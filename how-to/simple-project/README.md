
# field-line-experiments

A minimal repository that has features recommended for a small project. These features are described in the PyHC 2024 Summer School ["How-To"](https://docs.google.com/document/d/1PntLwlVvPJiMEZ6hoTtuvqOG2OzufMq5_7nWxr8lbfY/edit#heading=h.22h0gh3t8dul) session.

The size and complexity of this project is at the threshold of where it makes sense to create a package and generalize and refactor the code.

# Install and Run

```
pip install scipy matplotlib
python main.py # See switches at top of file for options
python plot.py
```

The output file `main.log` shows a comparison of the field line solutions using `RK45` and `RK23`, which is generated when `main.py` is run with `compare_methods = True`.