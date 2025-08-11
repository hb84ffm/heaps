# Proof that heap runtime is of $`O(log(n))`$ <br>

A heap (balanced binary tree) is a tree that carries for each parent (node) a maximum of  $`2`$ children, while last level always occurs without children and is called leave.The runtime boundary for such a heap is in worst case $`O(log(n))`$.<br><br>
We give a short proof sketchfor this by:

(a) deriving the general formula of such a "worst case" balancing operation (root to leave!)  
(b) show that the formula has a boundary of $`O(log(n))`$.<br>

With $`n`$ we refer to the number of inputs into the algorithm.

## (a) Derive the general formula
1. Assuming the tree has $`n+1`$ nodes ($`i=0,...,n`$), given by <br><br>
   $`i=0`$ with $`2^{0}=1`$ node <br>
   $`i=1`$ with $`2^{1}=2`$ nodes <br>
   $`...`$ <br>
   $`i=n`$ with $`2^{n}`$ nodes <br>
   
2. If we balance the worst case path (root to leave) we must sum all possible levels given by<br><br>
   $`\displaystyle\sum_{i=0}^{n}2^i`$<br> 
   We set this formula to:<br>
   
   (1) $`\displaystyle\sum_{i=0}^{n}2^i=2^{n+1}-1`$

   and proof it next, by induction.
   
3. **START**<br> 
    $`n=0`$ gives $`1=2^{0}=1=2^{0+1}-1=2^{1}-1=1`$

   **ASSUMPTION**<br>
   By **START** holds (1), hence we assume (1) also holds for general $`n`$.
   
   **INDUCTION**<br>
   To show that (1) also holds for $`n`$ $`\rightarrow`$ $`n+1`$, we must show that we fulfill<br>
   $`\displaystyle\sum_{i=0}^{n+1}2^i=2^{n+2}-1`$<br>
   
   Rewriting the sum we get<br>
   $`\displaystyle\sum_{i=0}^{n}2^i+2^{n+1}=2^{n+2}-1`$<br><br>
   and we know that for the left sum we can use (1), hence we get<br>
   $`(2^{n+1}-1)+2^{n+1}=2^{n+2}-1`$<br>
   
   now rearranging left side hand we get<br>
   $`2^{n+1}+2^{n+1}-1=2^{n+2}-1`$<br>
   
   which gives<br>
   $`2*2^{n+1}-1=2^{n+2}-1`$<br>
   
   and finally<br>
   $`2^{n+1}-1=2^{n+2}-1`$<br>
   
   to proof that (1) holds.<br><br>

##  (b) Derive $`O(log(n))`$ 
We assume  $`n>0`$ to not proof a trivial case and avoid the term   $`log(0)`$.<br>  
We now know that each $`n`$ node binary tree has a worst case balancing of<br>
   $`2^{n+1}-1`$<br>
Now to find height  $`i`$ in terms of $`n`$ input's we write $`n=2^{i+1}-1`$  which gives  $`n+1=2^{i+1}`$, applying logarithm gives<br>
$`i=\frac{1}{log(2)}*log(n+1)-1`$ now ignoring constants $`\frac{1}{log(2)}`$, $`1`$ and $`-1`$ we can say that $`i`$ is as of $`O(log(n))`$ 
