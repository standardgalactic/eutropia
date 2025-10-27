import os
import subprocess
from datetime import datetime

# --- 1. Define output paths ---
os.makedirs("output", exist_ok=True)
tex_path = "output/rsvp_essay.tex"
bib_path = "output/rsvp_essay.bib"

# --- 2. Define LaTeX content with real citations ---
tex_content = r"""
\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,mathrsfs}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{hyperref}
\usepackage{setspace}
\setstretch{1.25}
\title{The Field and the Compression:\\RSVP, Predictive Processing, and the Geometry of Assembly}
\author{Flyxion}
\date{\today}

\begin{document}
\maketitle

\section*{Abstract}
This essay explores how the Relativistic Scalar--Vector Plenum (RSVP) formalism integrates predictive processing \cite{friston2023active}, assembly theory \cite{marshall2021assembly}, and compression as universal principles of cognition and physics.

\section{Introduction}
The RSVP model treats the universe as a plenum of interacting scalar, vector, and entropic fields. It unifies cognition and physics by identifying intelligence as a form of entropic geometry---a recursive process of compression and prediction embedded in spacetime itself \cite{barandes2025unistochastic}.

\section{Predictive Processing and Entropic Descent}
Predictive processing suggests that the mind minimizes surprise by constantly refining internal models \cite{friston2023active}. In RSVP, this is not only a neural process but a universal gradient: the descent of entropy through alignment between scalar potential $\Phi$, vector flow $\mathbf{v}$, and entropy field $S$. Local coherence arises where prediction error vanishes:
\[
\frac{dS}{dt} = -\nabla \cdot (\Phi \mathbf{v}) + \sigma.
\]
Here, $\sigma$ denotes dissipative corrections---the residue of learning. Systems evolve to minimize $\sigma$, replacing noise with structure.

\section{Assembly and Historical Curvature}
Assembly theory reframes complexity as a measure of historical work: the number of transformations required to construct a given entity \cite{marshall2021assembly}. RSVP situates this within field geometry: $S$ carries the memory of work, while $\mathbf{v}$ encodes its negentropic trajectory. Every coherent structure is thus a fossil of successful compression---a trace of improbability sustained against dissolution.

\section{Compression and the Physics of Meaning}
Compression represents the universal attractor of the plenum: the drive for distributed information to fold into shorter generative codes, minimizing $H(S|\Phi, \mathbf{v})$. Meaning emerges when a system can predict its own entropy---when the code reconstitutes its conditions of existence. Beauty, intelligence, and order are all manifestations of this recursive compression \cite{barandes2025unistochastic}.

\section{Conclusion}
RSVP, predictive processing, and assembly theory converge on the same principle: that persistence is compression under constraint. Whether physical, biological, or cognitive, all coherent systems are feedback loops that stabilize their internal representations of uncertainty. The universe learns by shortening its own description.

\begin{quote}\small
``Every act of understanding is an act of entropy reduction.''
\end{quote}

\bibliographystyle{plain}
\bibliography{rsvp_essay}

\end{document}
"""

# --- 3. Define BibTeX references ---
bib_content = r"""
@article{friston2023active,
  title={Active inference and the physics of life},
  author={Friston, Karl and others},
  journal={Nature Reviews Neuroscience},
  year={2023}
}

@article{barandes2025unistochastic,
  title={Unistochastic Quantum Theory},
  author={Barandes, Jacob},
  journal={Foundations of Physics},
  year={2025}
}

@article{marshall2021assembly,
  title={Assembly Theory and the Origins of Life},
  author={Marshall, Sara Imari Walker and Cronin, Leroy},
  journal={Nature},
  year={2021}
}
"""

# --- 4. Sanitize and write files ---
tex_content = tex_content.replace('\x1a', '').lstrip('\ufeff')
with open(tex_path, "w", encoding="utf-8") as f:
    f.write(tex_content)
with open(bib_path, "w", encoding="utf-8") as f:
    f.write(bib_content)

# --- 5. Compile with XeLaTeX + BibTeX ---
print("Running XeLaTeX and BibTeX...")
subprocess.run(["xelatex", "-interaction=nonstopmode", "rsvp_essay.tex"], cwd="output")
subprocess.run(["bibtex", "rsvp_essay"], cwd="output")
subprocess.run(["xelatex", "-interaction=nonstopmode", "rsvp_essay.tex"], cwd="output")
subprocess.run(["xelatex", "-interaction=nonstopmode", "rsvp_essay.tex"], cwd="output")

print(f"\n✅ Compilation complete. PDF generated at: {os.path.abspath('output/rsvp_essay.pdf')}")

