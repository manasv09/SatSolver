<!DOCTYPE html>
<html>

<body class="stackedit">
  <div class="stackedit__html"><p><a href="http://Readme.md">Readme.md</a><sup class="footnote-ref"><a href="#fn1" id="fnref1">1</a></sup></p>
<h1 id="sat-solver">SAT-SOLVER</h1>
<p><strong>A python3 implementation of the famous NP-Complete “Satisfiability Solver” problem.</strong></p>
<p><strong>Instructions to use -</strong></p>
<ul>
<li>Generate a text file from problem CNF, for which the satisfiability is to be tested, in the given format</li>
<li>Sample CNF = (A + ~B) (~A + B) (C + A)</li>
<li>Input file-</li>
</ul>
<pre><code>A ~B
~A B
C A
</code></pre>
<ul>
<li>Save the file with the name &lt;input_file&gt;</li>
<li>In the terminal run the command given below</li>
</ul>
<pre><code>python3 SatSolver.py &lt;input_file&gt;
</code></pre>
<p><strong>Sample Output -</strong></p>
<ul>
<li>For the above example the output is displayed like this-</li>
</ul>
<pre><code>Original CNF:= (A + B̅)(C + A)(A̅ + B)


Initial CNF:= (A + B̅)(C + A)(A̅ + B)
Updated CNF:= (A + B̅)(C + A)(A̅ + B)
Unit Clauses:= ()


Initial CNF:= (A + B̅)(A)(C + A)(A̅ + B)
Updated CNF:= (B)
Unit Clauses:= (A)


Initial CNF:= (B)
Updated CNF:= ()
Unit Clauses:= (B)


		Result: SATISFIABLE
		Solution: (A)(B)
</code></pre>
<hr class="footnotes-sep">
<section class="footnotes">
<ol class="footnotes-list">
<li id="fn1" class="footnote-item"><p>Author: Manas Vashistha <a href="#fnref1" class="footnote-backref">↩︎</a></p>
</li>
</ol>
</section>
</div>
</body>

</html>
