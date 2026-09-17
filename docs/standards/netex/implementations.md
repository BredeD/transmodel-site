# NeTEx — Implementations

NeTEx is used across Europe through a set of **national profiles**. A profile picks a subset of the full NeTEx standard, fixes the codesets for a given country's context, and documents national extensions. Every European National Access Point runs on the profile that fits its country.

## How profiles relate to the European baseline

Most published profiles align with one of two European reference points:

- **EPIP-based** — the profile was specified against the European Passenger Information Profile (EPIP), the CEN-published minimum profile for the MMTIS obligations of national access points.
- **EPIP-compatible** — the profile was specified independently (usually earlier), but has been demonstrated to interoperate with EPIP, sometimes via conversion.

Some profiles are neither — they were built for a specific national scope that doesn't map to EPIP one-to-one. The distinction matters when planning cross-border data flow.

## Published profiles

| Country | Status | EPIP-based | EPIP-compatible | Documentation |
| --- | --- | :---: | :---: | --- |
| Austria | Specified, not yet in operation | ✅ |  | [Austrian profile](https://mobilitaetsverbuende.atlassian.net/wiki/spaces/NET/overview) |
| Belgium | Specified, not yet in operation | ✅ |  | [OSLO mobility](https://github.com/Informatievlaanderen/OSLOthema-mobiliteitDienstregelingEnPlanning) · [timetables](https://purl.eu/doc/applicationprofile/netex-belgium/timetables-ap/) · [stops](https://purl.eu/doc/applicationprofile/netex-belgium/stopplaces-ap/) · [vehicle scheduling](https://purl.eu/doc/applicationprofile/netex-belgium/vehiclescheduling-ap/) |
| Croatia | Specified and in use | ✅ | ✅ | [Croatian NAP](https://www.promet-info.hr/en) |
| Czech Republic | Specified, not yet in operation | ✅ |  | — |
| Denmark | Specified, not yet in operation | ✅ |  | [Denmark profile](https://www.trafikstyrelsen.dk/Media/638013312835439194/Vejledning%20om%20brug%20af%20NeTEx.pdf) · [Danish NAP](https://www.trafikstyrelsen.dk/arbejdsomraader/kollektiv-trafik/statistik-og-data/krav-til-udstilling-af-data-til-rejseplanlaegning) |
| France | Specified and in use |  | ✅ | [French profile](https://normes.transport.data.gouv.fr/normes/netex/) (sub-profiles: [common](https://normes.transport.data.gouv.fr/normes/netex/elements_communs/), [stops](https://normes.transport.data.gouv.fr/normes/netex/arrets/), [network](https://normes.transport.data.gouv.fr/normes/netex/reseaux/), [timetable](https://normes.transport.data.gouv.fr/normes/netex/horaires/), [fares](https://normes.transport.data.gouv.fr/normes/netex/tarifs/), [parking](https://normes.transport.data.gouv.fr/normes/netex/parkings/), [accessibility](https://normes.transport.data.gouv.fr/normes/netex/accessibilite/)) |
| Ireland | Specified and in use |  |  | [Irish profile](https://netex.ie/) · [profile elements](http://netex.uk/netexie/doc/EIRE_NP/NTA-NeTEx-1-Spec-2020.08.12-v0.22.pdf) · [mappings](http://netex.uk/netexie/doc/EIRE_NP/NTA-NeTEx-2-Mappings-2020.08.06-v0.22.pdf) |
| Italy | Specified and in use | ✅ |  | [Italian profile](https://github.com/5Tsrl/netex-italian-profile/tree/main/Linee%20guida) |
| Netherlands | Specified, not yet in operation | ✅ |  | [Dutch profile](https://bison.dova.nu/standaarden/nederlands-netex-profiel) · [Bison fares](https://bison.dova.nu/sites/default/files/bison_prijzen_producten_en_tarieven_v8.1.3.0_release.pdf) |
| Nordic (NO / SE / FI / DK) | Specified and in use |  | ✅ | [Nordic profile](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/728891481/Nordic+NeTEx+Profile) |
| Portugal | Specified and in use |  |  | [Portuguese profile](https://ptprofiles.azurewebsites.net/netex-profile) |
| Slovenia | Specified, not yet in operation |  | ✅ | [Slovenian profile](https://www.nap.si/_resources/profiles/NeTEx_SI_Profile_v2.pdf) |
| Switzerland | Specified and in use |  |  | [Swiss profile](https://www.oev-info.ch/sites/default/files/2024-05/NeTEx_Core-Realisation_Guide_TP_Suisse-v1.00.pdf) |
| United Kingdom | Specified and in use |  | ✅ | [UK profile](http://netex.uk/farexchange/) · [intro](http://netex.uk/farexchange/doc/uk_profile/DfT-NeTEx-1-Fares-Intro-2019.06.17-v0.09.pdf) · [stops & timetables](http://netex.uk/farexchange/doc/uk_profile/DfT-NeTEx-2-Base_Spec-2019.06.30-v0.14.pdf) · [fares](http://netex.uk/farexchange/doc/uk_profile/DfT-NeTEx-3-Fares_Spec-2019.06.17-v0.17.pdf) |

Australia (Victoria) has also adopted an EPIP-based profile outside CEN's jurisdiction; it is not listed above to keep the focus on European profiles.

This inventory was originally maintained by the Data4PT project (ended June 2025). To propose a change, see [How to contribute](../../introduction/how-to-contribute.md).

## MMTIS data categories

The **MMTIS Regulation ((EU) 2024/490)** defines four *Levels of Service* (LOS 1–4) that public transport data must meet at national access points. Each national profile covers some or all of these levels:

- **LOS 1** — location search, calendars, trip plans
- **LOS 2** — actual passing times, service alerts, static vehicle availability
- **LOS 3** — special conditions (luggage, wheelchair access), booking/ticketing
- **LOS 4** — real-time occupancy, disruption alerts, service change management

The most complete profiles today cover LOS 1–2 in full and much of LOS 3. LOS 4 (real-time) is generally handled via SIRI rather than NeTEx. A compatibility matrix mapping each profile against LOS 1–4 will be added here once cross-profile validation is complete.

## Related profiles

Beyond national profiles, two European profiles play a coordinating role:

- **EPIP** — the CEN-published minimum profile for MMTIS obligations, in the [CEN NeTEx repository](https://github.com/TransmodelEcosystem/NeTEx).
- **EFRP / EFIP** — the emerging European Fare Rail Profile and European Fare Information Profile, coordinated through CEN/TC 278 for cross-border rail fare and ticketing data.

## Adding a profile

A profile can be listed here once it is publicly documented and has a maintainer. Open a pull request or contact the [team](../../contact/team.md).
