<div align="center">

<br>

# D I N E T H &nbsp;&nbsp; N E T H S A R A

<br>

**Engineering at the boundary of signals, systems, and learned representations.**

<br>

![University of Peradeniya](https://img.shields.io/badge/University%20of%20Peradeniya-Electronics%20%26%20Electrical%20Eng.-7BA7BC?style=flat-square&labelColor=0F1623)&nbsp;&nbsp;![IEEE IGARSS 2026](https://img.shields.io/badge/IEEE%20IGARSS%202026-Accepted-8A9E8C?style=flat-square&labelColor=0F1623)&nbsp;&nbsp;![Founder](https://img.shields.io/badge/Founder-Tech%20Startup-7BA7BC?style=flat-square&labelColor=0F1623)

<br>

</div>

---

<br>

### About

<table>
<tr>
<td width="50%" valign="top">

**The Researcher**

My research sits at the intersection of state space models and remote sensing — specifically, how selective scan mechanisms like Mamba can replace attention in dense prediction tasks on satellite imagery. This started with a systematic study of frequency-domain transforms for segmentation, where I benchmarked DCT, wavelets, and nonsubsampled shearlets across hundreds of image decompositions. That work pointed directly at the limitations of isotropic feature extraction and led to the architecture now accepted at IEEE IGARSS 2026. I think carefully about what representations a model actually needs, and I build from that understanding.

</td>
<td width="50%" valign="top">

**The Builder**

Outside the lab, I build things that ship. I am co-founding a tech startup while finishing my degree — the kind of work that teaches you how little separates a working prototype from a production system, and how much separates both from a demo. Separately, I run raceday.lk, a motorsport media brand that started on Instagram and is growing into a full editorial platform. My embedded work — ESP32 audio classifiers, omnidirectional robots, real-time DSP pipelines — comes from the same instinct: I care about systems that run on real hardware, under real constraints.

</td>
</tr>
</table>

A fuller picture of my work and thinking is at [dineth.dev](https://dineth.dev) ↗

<br>

---

<br>

### Research

> #### Visual State Space Models for Remote Sensing Image Segmentation
>
> <sub>IEEE IGARSS 2026 · International Geoscience and Remote Sensing Symposium</sub>
>
> Proposes a Mamba-based architecture for dense semantic segmentation of satellite imagery, replacing self-attention with selective state space scanning to achieve linear-complexity inference on high-resolution remote sensing inputs.
>
> <!-- Links will be updated upon publication at IGARSS 2026 -->
> [![Paper ↗](https://img.shields.io/badge/Paper-Forthcoming-C4956A?style=flat-square&labelColor=0F1623)](#)&nbsp;&nbsp;[![Code ↗](https://img.shields.io/badge/Code-Forthcoming-C4956A?style=flat-square&labelColor=0F1623)](#)

Current open questions I am working through: how to encode multi-temporal structure into state space scans without collapsing temporal invariance, and whether shearlet-domain priors can regularize SSM feature maps at the boundary level.

<br>

---

<br>

### Projects & Repositories

<table>
<tr>
<td width="50%" valign="top">

[**elephant-detection-system-using-infrasound-vibrations**](https://github.com/Dineth14/elephant-detection-system-using-infrasound-vibrations)
<br>
<sub>Real-time elephant detection via infrasound analysis and k-NN classification on ESP32</sub>
<br><br>
![Python](https://img.shields.io/badge/-Python-8A9E8C?style=flat-square)&nbsp;![Stars](https://img.shields.io/github/stars/Dineth14/elephant-detection-system-using-infrasound-vibrations?style=flat-square&label=%E2%98%85&labelColor=0F1623&color=8B93A8)

</td>
<td width="50%" valign="top">

[**ESP32-Real-Time-Noise-Logger**](https://github.com/Dineth14/ESP32-Real-Time-Noise-Logger)
<br>
<sub>Audio classification with 30 kHz sampling, digital filtering, and offline k-NN on ESP32</sub>
<br><br>
![Python](https://img.shields.io/badge/-Python-8A9E8C?style=flat-square)&nbsp;![Stars](https://img.shields.io/github/stars/Dineth14/ESP32-Real-Time-Noise-Logger?style=flat-square&label=%E2%98%85&labelColor=0F1623&color=8B93A8)

</td>
</tr>
<tr>
<td width="50%" valign="top">

[**XLET-NSST**](https://github.com/Dineth14/XLET-NSST)
<br>
<sub>Optimal frequency channel selection for image segmentation via nonsubsampled shearlet transforms</sub>
<br><br>
![Python](https://img.shields.io/badge/-Python-8A9E8C?style=flat-square)&nbsp;![Stars](https://img.shields.io/github/stars/Dineth14/XLET-NSST?style=flat-square&label=%E2%98%85&labelColor=0F1623&color=8B93A8)

</td>
<td width="50%" valign="top">

[**transform-generations-segmentation-analysis**](https://github.com/Dineth14/transform-generations-segmentation-analysis)
<br>
<sub>Comparative framework — DCT vs wavelets vs XLET-NSST for remote sensing segmentation</sub>
<br><br>
![Python](https://img.shields.io/badge/-Python-8A9E8C?style=flat-square)&nbsp;![Stars](https://img.shields.io/github/stars/Dineth14/transform-generations-segmentation-analysis?style=flat-square&label=%E2%98%85&labelColor=0F1623&color=8B93A8)

</td>
</tr>
<tr>
<td width="50%" valign="top">

[**wavelets-and-contourlets**](https://github.com/Dineth14/wavelets-and-contourlets)
<br>
<sub>DWT, DT-CWT, and NSCT comparison for image denoising and edge detection</sub>
<br><br>
![Python](https://img.shields.io/badge/-Python-8A9E8C?style=flat-square)&nbsp;![Stars](https://img.shields.io/github/stars/Dineth14/wavelets-and-contourlets?style=flat-square&label=%E2%98%85&labelColor=0F1623&color=8B93A8)

</td>
<td width="50%" valign="top">

[**Omni-robot**](https://github.com/Dineth14/Omni-robot)
<br>
<sub>4-wheel omnidirectional robot with Jetson Nano and standalone Python control</sub>
<br><br>
![Python](https://img.shields.io/badge/-Python-8A9E8C?style=flat-square)&nbsp;![Stars](https://img.shields.io/github/stars/Dineth14/Omni-robot?style=flat-square&label=%E2%98%85&labelColor=0F1623&color=8B93A8)

</td>
</tr>
</table>

<br>

#### Live Deployments

**raceday.lk** — Motorsport media and editorial platform · [Live ↗](https://raceday.lk)<br>
**dineth.dev** — Portfolio and project archive · [Live ↗](https://dineth.dev)

<br>

---

<br>

### Technical Depth

| Domain | Stack | Context |
|:-------|:------|:--------|
| Computer Vision & ML | ![PyTorch](https://img.shields.io/badge/-PyTorch-7BA7BC?style=flat-square&labelColor=0F1623) · Mamba · Transformers | Research-grade |
| Embedded Systems | ![ESP32](https://img.shields.io/badge/-ESP32-8A9E8C?style=flat-square&labelColor=0F1623) · FreeRTOS · Arduino | Project-level |
| Signal Processing | MATLAB · DSP · Comm Systems | Applied + coursework |
| Power Engineering | Simulink · Simscape | Coursework + lab |
| Languages | ![Python](https://img.shields.io/badge/-Python-7BA7BC?style=flat-square&labelColor=0F1623) · ![C/C++](https://img.shields.io/badge/-C%2FC%2B%2B-7BA7BC?style=flat-square&labelColor=0F1623) · MATLAB | — |
| Tools & Infra | Git · Linux · LaTeX · VS Code | — |

<br>

---

<br>

### GitHub Intelligence

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Dineth14&show_icons=true&bg_color=0A0E17&title_color=7BA7BC&text_color=D8DCE8&border_color=1C2333&icon_color=C4956A&hide_border=false" height="180" alt="GitHub stats" />
  &nbsp;&nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Dineth14&layout=compact&bg_color=0A0E17&title_color=7BA7BC&text_color=D8DCE8&border_color=1C2333&icon_color=C4956A&hide_border=false" height="180" alt="Top languages" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=Dineth14&background=0A0E17&border=1C2333&stroke=1C2333&ring=C4956A&fire=C4956A&currStreakNum=D8DCE8&sideNums=D8DCE8&currStreakLabel=7BA7BC&sideLabels=7BA7BC&dates=8B93A8" height="180" alt="GitHub streak" />
</p>

<br>

---

<br>

### Connect

<p align="center">

[![Email](https://img.shields.io/badge/Email-dp18perera%40gmail.com-1C2333?style=flat-square&logo=gmail&logoColor=7BA7BC&labelColor=1C2333)](mailto:dp18perera@gmail.com)&nbsp;&nbsp;[![LinkedIn](https://img.shields.io/badge/LinkedIn-Dineth%20Nethsara-1C2333?style=flat-square&logo=linkedin&logoColor=7BA7BC&labelColor=1C2333)](https://linkedin.com/in/dineth-perera-ba9657277)&nbsp;&nbsp;[![Instagram](https://img.shields.io/badge/Instagram-raceday.lk-1C2333?style=flat-square&logo=instagram&logoColor=7BA7BC&labelColor=1C2333)](https://instagram.com/raceday.lk)&nbsp;&nbsp;[![Portfolio](https://img.shields.io/badge/Portfolio-dineth.dev-1C2333?style=flat-square&logo=safari&logoColor=7BA7BC&labelColor=1C2333)](https://dineth.dev)

</p>

<br>

<p align="center">
<sub><i>Most of what I know, I learned by building something that didn't work the first time.</i></sub>
</p>
