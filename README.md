# idena data collector

Uses Endogen's Idena API for Python to record your Idena balance over time.

### Scripts:

- `dna_calc.py`: Script to get time and balance data from a csv file and display a graph of your balance with time, and calculate DNA/day and $/day.

- `dna_watcher.py`: Fetches your current balance every hour (unless changed in `dna_config.py`). Recommended to be run alongside the idena node.

### Configuration:

`dna_config.py` contains configurable variables. Instructions included inside.

### Dependencies:

- `pycoingecko`, `numpy`, `matplotlib`. These can be installed via Python's `pip`:

```
pip install --user pycoingecko numpy matplotlib
```

### Running:

Run with Python 3, and make sure dependencies are installed, and you have changed `dna_config.py` to fit your setup.

I recommend running `dna_watcher.py` on startup, and running `dna_calc.py` whenever you want to see a graph of your balance.

