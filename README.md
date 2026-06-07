# waveshareLCD

A Raspberry Pi project that displays system information and a custom logo on a Waveshare 1.44" LCD HAT, with systemd service support for auto-start on boot.

## Overview

A customized version of the Waveshare LCD sample code that displays Pi system information (CPU, memory, temperature, etc.) along with a custom logo on the [Waveshare 1.44inch LCD HAT](https://www.waveshare.com/wiki/1.44inch_LCD_HAT).

## Hardware Requirements

- Raspberry Pi (any model with 40-pin GPIO header)
- [Waveshare 1.44inch LCD HAT](https://www.waveshare.com/wiki/1.44inch_LCD_HAT) (128x128 pixels, ST7735S driver)

## Prerequisites

- Raspberry Pi OS
- Python 3.x
- SPI enabled (`sudo raspi-config` → Interface Options → SPI)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Boon67/waveshareLCD.git
   cd waveshareLCD
   ```

2. Install LCD drivers:
   ```bash
   chmod +x install_drivers.sh
   ./install_drivers.sh
   ```

3. Run the display:
   ```bash
   python main.py
   ```

## Auto-Start on Boot

To configure the LCD display as a systemd service:

```bash
chmod +x deployservice.sh
./deployservice.sh
```

This installs `lcddisplay.service` to start the display on boot.

## Project Structure

```
├── main.py              # Main display program
├── LCD_1in44.py         # LCD driver (ST7735S)
├── LCD_Config.py        # SPI/GPIO configuration
├── gpio_inputs.py       # Button/GPIO input handling
├── install_drivers.sh   # Waveshare driver installer
├── deployservice.sh     # Systemd service installer
├── lcddisplay.service   # Service unit file
└── logo.png             # Custom logo displayed on LCD
```

## Customization

- Replace `logo.png` with your own 128x128 pixel image
- Modify `main.py` to change displayed system information

## License

MIT - see [LICENSE](LICENSE)
