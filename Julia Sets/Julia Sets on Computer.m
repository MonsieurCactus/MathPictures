(* ::Package:: *)

(* ::Title:: *)
(*Attempts at Drawing Julia Sets*)


(* ::Text:: *)
(**)


(* ::Subtitle:: *)
(*Dendrite*)


(* ::Input:: *)
(*Clear[z,w,f]*)
(*iterations = 100000;*)
(*f[z_]:=z^2+I;*)
(*w = (1 + Sqrt[1-4I])/2;*)
(*complexpts=Table[*)
(*(w = N[If[RandomInteger[1]==0,1,-1]]Sqrt[w-I];N[w])*)
(*,{k,1,iterations}];*)
(*dendritepts= Table[{Re[#],Im[#]}&[complexpts[[k]]],{k,1,iterations}];*)


(* ::Input:: *)
(*ListPlot[%, AspectRatio -> Automatic]*)


(* ::Subtitle:: *)
(*Airplane*)


(* ::Input:: *)
(*Clear[z,w,f]*)
(*iterations = 100000;*)
(*c = -1.75488;*)
(*f[z_]:=z^2-I;*)
(*w = (1 + Sqrt[1-4c])/2;*)
(*complexpts=Table[*)
(*(w = N[If[RandomInteger[1]==0,1,-1]]Sqrt[w-c];N[w])*)
(*,{k,1,iterations}];*)
(*dendritepts= Table[{Re[#],Im[#]}&[complexpts[[k]]],{k,1,iterations}];*)


(* ::Input:: *)
(*ListPlot[%, AspectRatio -> Automatic]*)


(* ::Subtitle:: *)
(*Spiral Cantor Set*)


(* ::Input:: *)
(*Clear[z,w,f]*)
(*iterations = 1000000;*)
(*c = -0.765+0.12I;*)
(*f[z_]:=z^2-I;*)
(*w = (1 + Sqrt[1-4c])/2;*)
(*complexpts=Table[*)
(*(w = N[If[RandomInteger[1]==0,1,-1]]Sqrt[w-c];N[w])*)
(*,{k,1,iterations}];*)
(*dendritepts= Table[{Re[#],Im[#]}&[complexpts[[k]]],{k,1,iterations}];*)


(* ::Input:: *)
(*ListPlot[%, AspectRatio -> Automatic]*)


(* ::Subtitle:: *)
(*Douady Rabbit*)


(* ::Input:: *)
(*Clear[z,w,f]*)
(*iterations = 100000;*)
(*c = -0.122+0.745I;*)
(*f[z_]:=z^2-I;*)
(*w = (1 + Sqrt[1-4c])/2;*)
(*complexpts=Table[*)
(*(w = N[If[RandomInteger[1]==0,1,-1]]Sqrt[w-c];N[w])*)
(*,{k,1,iterations}];*)
(*dendritepts= Table[{Re[#],Im[#]}&[complexpts[[k]]],{k,1,iterations}];*)


(* ::Input:: *)
(*ListPlot[dendritepts, AspectRatio-> Automatic]*)


(* ::Subtitle:: *)
(*A Rational Function*)


(* ::Input:: *)
(*Clear[z,w,f]*)
(*iterations = 100000;*)
(*c = -0.122+0.745I;*)
(*f[z_]:=1 - 1/z^2;*)
(*w = 2;*)
(*complexpts=Table[*)
(*(w = N[If[RandomInteger[1]==0,1,-1]]/Sqrt[1-w];N[w])*)
(*,{k,1,iterations}];*)
(*dendritepts= Table[{Re[#],Im[#]}&[complexpts[[k]]],{k,1,iterations}];*)


(* ::Input:: *)
(*ListPlot[dendritepts, AspectRatio -> Automatic]*)
