# Applikationskod för P01: Sinusrekonstruktion med DAC
 Applikation med drivers för laborationen.

## Struktur
* **DAC-driver** ([dac.h](math_project/include/driver/dac.h) och [dac.c](math_project/source/driver/dac.c)): Initierar DAC:en och skriver/läser sampelvärden.
* **Sampler-driver** ([sampler.h](math_project/include/driver/sampler.h) och [sampler.c](math_project/source/driver/sampler.c)): Matar ut en sekvens av sampelvärden till DAC:en med given samplingsfrekvens.
* **[main.c](./math_project/main.c)**: Applikationens startpunkt. Detta är filen ni ska modifiera; ersätt exempelsamplen och samplingsfrekvensen med era egna beräknade värden.

Befintliga drivers är färdiga och ska inte behöva ändras.

---

## Licens
Koden i denna katalog är licensierad under [MIT](./LICENSE), separat från kursmaterialets [CC BY 4.0](../../../LICENSE).

---
