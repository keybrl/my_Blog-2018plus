# 测试页

!!! Tip ""
    hhh

hhh 1/2

```sequence
Title: Here is a title
A->B: Normal line
B-->C: Dashed line
C->>D: Open arrow
D-->>A: Dashed open arrow
```

$$
\frac{n!}{k!(n-k)!} = \binom{n}{k}
$$

***I'm italic and bold* I am just bold.**

***I'm bold and italic!** I am just italic.*

^^hhh^^

Here is some {--*incorrect*--} Markdown.  I am adding this{++ here++}.  Here is some more {--text
 that I am removing--}text.  And here is even more {++text that I 
 am ++}adding.{~~

~>  ~~}Paragraph was deleted and replaced with some spaces.{~~  ~>

~~}Spaces were removed and a paragraph was added.

And here is a comment on {==some
 text==}. Substitutions {~~is~>are~~} great!

General block handling.

{--

* test remove
* test remove
* test remove
    * test remove
* test remove

--}

{++

* test add
* test add
* test add
    * test add
* test add

++}

```C++ tab=
#include <iostream>

int main() {
  std::cout << "Hello, world!\n";
  return 0;
}
```

```C# tab=
using System;

class Program {
  static void Main(string[] args) {
    Console.WriteLine("Hello, world!");
  }
}
```

- [ ] 1. hhh
- [ ] 2. hhh

``` linenums="2 2"
"""Some file."""
import foo.bar
import boo.baz
import foo.bar.baz
```