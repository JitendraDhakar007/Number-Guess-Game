# Number-Guess
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyttsx3 and datetime.

```bash
pip install pyttsx3
pip install datetime
```

## Usage

```python
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
hour = int(datetime.datetime.now().hour)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
