% Filename: blad.cls
% Author: Arno Lepisk
% Version: 1

% This is a LaTeX2e document class.

\NeedsTeXFormat{LaTeX2e}
 
\ProvidesClass{blad}[2003/01/24 Sangbladsklass]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}

\ProcessOptions

\LoadClass[a4paper]{article}

\RequirePackage[T1]{fontenc}        % används för att få svensk avstavning
\RequirePackage[swedish]{babel}     
%\RequirePackage[latin1]{inputenc}   % och å, ä ,ö


\RequirePackage{latexsym}
%\RequirePackage{fkm}
\RequirePackage{calc}
\RequirePackage{ifthen}

\RequirePackage{verbatim}

\setlength{\hoffset}{-1in}
\setlength{\topmargin}{5mm}
\setlength{\headsep}{0in}
\setlength{\headheight}{0in}

\setlength{\oddsidemargin}{6mm}
\setlength{\evensidemargin}{6mm}

\setlength{\voffset}{-1in}
\setlength{\lineskip}{0pt}
\setlength{\parindent}{0pt}
\setlength{\marginparwidth}{0pt}
\setlength{\marginparsep}{0pt}

\setlength{\paperwidth}{.5\paperwidth}

\setlength{\textwidth}{.96\paperwidth}
\setlength{\textheight}{.95\paperheight}


\newenvironment{sang}[1]{\startasang{#1}}{\slutasang}

\newcommand{\startasang}[1]{%
%\makebox{%
\nopagebreak%
\subsection*{#1}%
\begin{verse}%
%\begin{verbatim}%
}

\newcommand{\slutasang}{%
%\end{verbatim}%
\end{verse}%
\nopagebreak%
}

\pagenumbering{none}
\pagestyle{empty}






