# SENSITIVITY ANALYSIS CODE

## Important Variables

```python
calibrated_params = [guessed_value_for_a, guessed_value_for_b]
real_params = [realistic_value_for_a, realistic_value_for_b]
max_error_diff = maximum_allowable_error
```
Change the above variables as derired by the needs of the calibration routine.

## Methods
The method naming convention should be self explanatory

## Dependent Libraries

### global
scipy.optimize import Bounds

scipy.optimize import minimize

scipy.optimize import SR1

numpy, sys

### local
highway_free_flow 

## Usage
```
python maximize_a_calib.py
```
