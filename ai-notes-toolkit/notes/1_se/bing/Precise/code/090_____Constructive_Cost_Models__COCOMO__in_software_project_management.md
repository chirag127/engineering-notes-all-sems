### Constructive Cost Models (COCOMO) in software project management

COCOMO (Constructive Cost Model) is a model that allows software project managers to estimate the cost, effort, and schedule of a software project. It was first published by Barry Boehm in 1981 and has since been updated and refined.

Here is an example of how to calculate the effort and schedule using the Basic COCOMO model:

```python
def basic_cocomo(size, mode):
    if mode == 'organic':
        a = 2.4
        b = 1.05
        c = 2.5
        d = 0.38
    elif mode == 'semi-detached':
        a = 3.0
        b = 1.12
        c = 2.5
        d = 0.35
    elif mode == 'embedded':
        a = 3.6
        b = 1.20
        c = 2.5
        d = 0.32
    else:
        raise ValueError('Invalid mode')

    effort = a * (size ** b)
    schedule = c * (effort ** d)

    return effort, schedule
```

This function takes in the size of the project (in thousands of lines of code) and the mode of the project (organic, semi-detached, or embedded) and returns the estimated effort (in person-months) and schedule (in months).

For example, to estimate the effort and schedule for an organic project with a size of 32,000 lines of code, you would call the function like this:

```python
effort, schedule = basic_cocomo(32, 'organic')
```

This would return an estimated effort of 91.5 person-months and a schedule of 14.0 months.