"""
I/O Controller for BasCAT

Manages input and output operations through memory-mapped I/O.
- INPUT port at address 0xFF: Reads from input queue (FIFO)
- OUTPUT port at address 0xFE: Writes to output buffer
"""

from collections import deque
from src.core.signals import signals


class IOController:
    """
    I/O Controller manages input/output operations.

    Memory-mapped I/O:
    - 0xFE (254): OUTPUT port - write data here to display
    - 0xFF (255): INPUT port - read data from here
    """

    # Memory-mapped I/O addresses
    OUTPUT_PORT = 0xFE  # 254
    INPUT_PORT = 0xFF   # 255

    def __init__(self):
        # Input queue (FIFO) - stores bytes waiting to be read
        self.input_queue = deque()

        # Output buffer - stores all output for display
        self.output_buffer = []

        # Input status: True if data available
        self.input_available = False

    def reset(self):
        """Reset the I/O controller"""
        self.input_queue.clear()
        self.output_buffer.clear()
        self.input_available = False
        signals.output_cleared.emit()

    def write_output(self, value):
        """
        Write a byte to the OUTPUT port.
        This displays the value to the user.

        Args:
            value: 8-bit value to output (0-255)
        """
        value = value & 0xFF  # Ensure 8-bit
        self.output_buffer.append(value)

        # Emit signal for GUI update
        signals.output_written.emit(value)

        # Also emit as character if printable ASCII
        if 32 <= value <= 126:  # Printable ASCII range
            signals.output_char_written.emit(chr(value))

    def read_input(self):
        """
        Read a byte from the INPUT port.
        Returns the next byte from the input queue, or 0 if empty.

        Returns:
            int: 8-bit value from input queue, or 0 if empty
        """
        if self.input_queue:
            value = self.input_queue.popleft()

            # Update input available status
            self.input_available = len(self.input_queue) > 0

            # Emit signal that input was consumed
            signals.input_consumed.emit()

            return value & 0xFF
        else:
            # No input available - could block here or return 0
            # For now, return 0 (could also emit input_requested signal)
            signals.input_requested.emit()
            return 0

    def queue_input(self, value):
        """
        Add a byte to the input queue.
        This is called by the GUI when user provides input.

        Args:
            value: 8-bit value to queue (0-255)
        """
        value = value & 0xFF
        self.input_queue.append(value)
        self.input_available = True

        # Emit signal for GUI update
        signals.input_queued.emit(value)

    def queue_string(self, text):
        """
        Queue a string as a series of bytes.
        Converts each character to its ASCII value.

        Args:
            text: String to queue
        """
        for char in text:
            self.queue_input(ord(char))

    def get_output_as_string(self):
        """
        Get the complete output buffer as a string.
        Interprets bytes as ASCII characters.

        Returns:
            str: Output buffer as string
        """
        # Convert bytes to characters, replacing non-printable with '?'
        chars = []
        for byte_val in self.output_buffer:
            if 32 <= byte_val <= 126:  # Printable ASCII
                chars.append(chr(byte_val))
            elif byte_val == 10:  # Newline
                chars.append('\n')
            elif byte_val == 13:  # Carriage return
                chars.append('\r')
            elif byte_val == 9:  # Tab
                chars.append('\t')
            else:
                chars.append('?')  # Non-printable
        return ''.join(chars)

    def has_input(self):
        """
        Check if input is available.

        Returns:
            bool: True if input queue is not empty
        """
        return self.input_available
