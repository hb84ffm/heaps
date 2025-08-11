# Proof that heap runtime is of $`O(log(n))`$ <br>

A heap (balanced binary tree) is a tree that carries for each parent (node) a maximum of  $`2`$ children, while last level always occurs without children and is called leave.The runtime boundary for such a heap is in worst case $`O(log(n))`$.<br><br>
We give a short proof sketchfor this, by:

   (a) deriving the general formula of such a "worst case" balancing operation (root to leave!)  
   (b) show that the formula has a boundary of $`O(log(n))`$.<br>

We state that $`n`$ is the number of inputs to the algorithm.


(a) Derive general formula
1. Assuming the tree has $`n+1`$ nodes ($`i=0,...,n`$), given by <br><br>
   $`i=0`$ with $`2^{0}=1`$ node <br>
    $`i=1`$ with $`2^{1}=2`$ nodes <br>
    $`...`$ <br>
    $`i=n`$ with $`2^{n}`$ nodes <br>
2. If we now would balance the worst case path (root to leave), we would must sum all possible levels given by $`\displaystyle\sum_{i=0}^{n}2^i`$.<br> 
We flag this formula by (A) $`\displaystyle\sum_{i=0}^{n}2^i=2^{n+1}-1`$ and will proof it next by induction.
3. (START) $`n=0`$ gives $`2^{0}=1=2^{0+1}-1=2^{1}-1=1`$  <br>
   (ASSUMPTION) (A) holds therefore for general  $`n`$  <br>
   (INDUCTION) Show that (A)  also holds for $`n`$ $`\rightarrow`$ $`n+1`$. We must now show that we fulfill  $`\displaystyle\sum_{i=0}^{n+1}2^i=2^{n+2}-1`$<br>
Rewriting the sum we get  $`\displaystyle\sum_{i=0}^{n}2^i+2^{n+1}=2^{n+2}-1`$ and we know that for the left sum we can use  (A), hence we get <br>
 $`(2^{n+1}-1)+2^{n+1}=2^{n+2}-1`$ and now rearranging the left side hand we get $`2^{n+1}+2^{n+1}-1=2^{n+2}-1`$ which gives $`2*2^{n+1}-1=2^{n+2}-1`$ and finally
$`2^{n+1}-1=2^{n+2}-1`$ to proof that (A) holds.<br><br>

(b) Derive $`O(log(n))`$ 
1. Assuming  $`n>0`$ to not proof a trivial case and avoiding  $`log(0)`$ expression.  
2. We now know that each $`n`$ node binary tree has a worst case balancing of $`2^{n+1}-1`$. <br>
3. Now to find height  $`i`$ in terms of $`n`$ input's we write $`n=2^{i+1}-1`$  which gives  $`n+1=2^{i+1}`$, applying logarithm gives<br>
$`i=\frac{1}{log(2)}*log(n+1)-1`$ now ignoring constants $`\frac{1}{log(2)}`$, $`1`$ and $`-1`$ we can say that $`i`$ is as of $`O(log(n))`$ 
