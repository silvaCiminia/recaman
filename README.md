# Recamán

A basic python module for generating Recamán sequence variations and
some interesting graphs of those sequences.

## Usage

`recaman.seq(length, origin)`

To generate a sequence of the given length, starting the sequence calculation at the origin. Returns the resulting sequence in a tuple together with the highest number contained in the sequence, which can then be fed into `val_plot` or `circles` to produce some nice visualizations.

For instance, `circles(*seq(64, 0))` yields the first 64 members of the basic sequence:

![img0](img/64_0.png)

A change of origin with `seq(64, 32)` produces a graph with some interesting differences and definite endpoint. Due to the way the sequence works, starting at an origin other than zero introduces the possibility of a finite sequence:

![img1](img/64_32.png)

As you can see again with origin 64:

![img2](img/64_64.png)

Interesting patterns emerge almost immediately! For instance, look at this plot of origin points to resulting sequence lengths for an (attempted) 128 member sequence:

![img3](img/lengths.png)

Starting at x = 3, an interesting pattern emerges - triplets of the multiples of three, separated by a constantly incrementing number of values!

For more information on the Recamán sequence, see the entry in the [Online Encyclopedia of Integer Sequences](https://oeis.org/wiki/Recam%C3%A1n%27s_sequence). 
This project only deals with type 1 sequences, though it could easily be adapted to the other types by changing the operations in the `seq()` method.
