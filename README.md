# raspberrypi-pin-onoff

Simple python script to turn pins on and off on a Raspberry Pi 2 B+, used for quick testing/development.

Can take a comma separated list of pins, a range of pins, or a combination of the two.

## Supported Platforms

Raspberry Pi 2 B+

## Attributes

<table>
  <tr>
    <th>Key</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><tt>-p,--pins</tt></td>
    <td>String</td>
    <td>Switch to specify which pins to turn on from the command line</td>
  </tr>
</table>

## Usage

Basic Program flow:
* Enter Pins to turn on.
* The script turns them on and then loops in a sleep.
* Use Ctrl-C to quit and turn off the pin.

### python pi-pins.py

Run normally and get prompted for pins to turn on, use Ctrl-C to stop/quit:

```python
raspberrypi-pin-onoff $ sudo python ./pi-pins.py
Enter Pins (ex: 14,15-17,18)): 14
Pins: [14]
Running (Ctrl-C to quit)...
^C
Killing Thread...
```

Use command line option to specify pins from command line:
```python
raspberrypi-pin-onoff $ sudo python ./pi-pins.py --pins 14,17-19,23
Pins: [14, 17, 18, 19, 23]
Running (Ctrl-C to quit)...
^C
Killing Thread...
```

Command line can also take space separated list:
```python
raspberrypi-pin-onoff $ sudo python ./pi-pins.py --pins 14 17 23
Pins: [14, 17, 23]
Running (Ctrl-C to quit)...
^C
Killing Thread...
```

## License and Authors

Author:: Kevin Kingsbury (<kkingsbury@gmail.com>)
Apache 2.0
