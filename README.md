# notes-series-python
![LOGO](https://brandlogos.net/wp-content/uploads/2014/11/python-logo_brandlogos.net_cjulg.png)
### Learn python from basic every friday


## The zen of Python
Mastering the Zen of Python means carefully considering each piece of advice, even when the aphorisms may seem contradictory. The more you work with Python, the more intuitive these proverbs will become.

1. `Beautiful is better than ugly` | approachable and aesthetically pleasing syntax
```python
from math import sin

def sinusoid(A, ω, ϕ):
    return lambda t: A * sin(ω * t + ϕ)
```
This code reads almost like a mathematical formula thanks to Python’s compact syntax, which doesn’t get in your way. The use of Greek letters in variable names, so common in these types of equations, instantly makes the code relatable to anyone familiar with the underlying theory. Finally, the lambda expression makes the code concise while maintaining readability. As you can see, Python’s clarity and expressive power can be hard to beat.

2. `Explicit is better than implicit` | code need to be clear and easy to understand
```python
from math import sin
from typing import Callable, TypeAlias

Amplitude: TypeAlias = float
AngularFrequency: TypeAlias = float
PhaseShift: TypeAlias = float
Time: TypeAlias = float
SineWave: TypeAlias = Callable[[Time], float]

def sinusoid(A: Amplitude, ω: AngularFrequency, ϕ: PhaseShift) -> SineWave:
    """Return a function that computes the sine wave at a given time."""
    return lambda t: A * sin(ω * t + ϕ)
```
when you define a function, it’s much better to explicitly state the expected types of input parameters and the return value instead of forcing whoever reads your code to guess

3. `Simple is better than complex. Complex is better than complicated` | The simplest solutions are often the most elegant and efficient.

4. `Flat is better than nested. Sparse is better than dense` | keep things flat by avoiding deeply nested structures
```python
def dense(A, f, ϕ):
    return lambda t: A * sin(2 * π * f * t + ϕ)

def sparse(A, f, ϕ):
    ω = 2 * π * f
    return lambda t: A * sin(ω * t + ϕ)
```
Instead of using one long line of dense code, it’s usually better to spread the individual instructions out, making them easier to reason about. If you had multiple indentation levels nested inside one another, then it could quickly become cluttered and harder to follow.

5. `Now is better than never. Although never is often better than right now` | take action immediately, but always giving at least some thought.