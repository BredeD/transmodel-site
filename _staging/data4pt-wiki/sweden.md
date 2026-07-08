---
original_title: "Sweden"
source: mediawiki
source_url: https://data4pt.org/wiki/Sweden
last_edited: 2024-10-08T12:54:51Z
status: raw
---

## Overview in the National Level

The National project “Open Data” has been the foundation in implementing NeTEx and SIRI (Nordic Profile) in accordance with MMTIS in Sweden. The solution consists of an integration platform (STIP) where national imported Public Transport data in Noptis DOI/DII (Static data) and Noptis ROI (Realtime data) as well as Transport and MPK – proprietary formats, is translated into NeTEx and SIRI (as well as GTFS and GTFS-R). The translated data is published at the NAP (Trafiklab.se) and used within the National ticketing Distribution System as well as various traffic information services such as Skånetrafikens OTP2 (Open Trip Planner).

## Use cases

There are two main use cases in Sweden where Transmodel based standards are implemented and used.

1.  **National ticket Distribution System, Sweden** (all PTA´s and PTO´s). New national ticketing distribution based on booking standard OSDM with traffic data in NeTEx format.  Sweden is the first in Europe with a distributed ecosystem connected to multiple booking systems. The system is built on the open and international booking standard OSDM-Online, developed by the International Union of Railways (UIC). The system is fed with Public Transport data based on NeTEx (Nordic Profile). With this competition-neutral standards as a foundation, all producers in both Sweden and Europe have the opportunity to connect. Consequently, the system will have multiple booking systems linked to it. The system is being developed in collaboration with Turnit, an Estonian company with experience in standards within the railway industry in Europe.
2.  **Open Trip Planner Skåne, Sweden**. New trip planner developed on open standard OTP2 for regional travelling and cross boarder travelling purposes. Skåne is the 3rd largest region (PTA) in Sweden with Public Transport including city buses (incl. BRT) and regional trains.

### Architecture

#### National ticket Distribution System

The new **National ticket Distribution System, Sweden** infrastructure creates favorable conditions for the continued development of the ticket collaboration Resplus. The service will also enable more secure and widely validatable tickets when implemented. This, in turn, will contribute to increased safety and secured revenue. The system is being developed in collaboration with Turnit, an Estonian company with experience in standards within the railway industry in Europe. The new infrastructure is built on four essential components, with communication between these components based on the international and open OSDM-Online standard (Open Sales and Distribution Model).

1.  A "data warehouse" where the majority of Samtrafiken's partners will store their ticket products. This is where the offerings of transportation companies are entered, and it is from here that the service retrieves the inventory.
2.  The sales tool Samtrafiken TRAID and a sales API. In TRAID, retailers can directly book journeys, suitable for those retailers with a need for manual sales management (such as kiosks, stores, or call centers) or as a complement to web sales. Retailers and producers wishing to sell through their own sales tools (such as websites or apps) can choose to access the inventory via API.
3.  Travel search for all saleable ground-based collective transport.
4.  A central service, a so-called distribution hub, which retrieves, combines, and distributes ticket products from both Samtrafiken's data warehouse and external data warehouses for partners with their booking systems.

#### Open Trip Planner Skåne

**The Skåne OpenTripPlanner** (OTP2) is a server-side Java application that is primarily designed to interpret and combine map, transit service, and other mobility data sets, providing API endpoints that receive user origins and destinations and return trip plans to other applications along with vector map tiles, stop departures, and other rider information. In other words, OTP is a backend application that can work with other frontend user interfaces. OTP is an open standard and works with your website, mobile app, physical signage or other applications in order to provide relevant customer information and meaningful trip plans to riders.

### Outcome

The **National ticket Distribution System** and **Open Trip Planner Skåne OTP2** are implemented and in operation with minor operational problems to fix as well as ongoing further developments. Both implementations are built on open and international standards provided with Public Transport data like NeTEx and Siri. With this competition-neutral standards as a foundation, all producers in both Sweden and Europe have the opportunity to connect. This provides significant benefits for travelers, making it easier to access, plan, and book train journeys with multiple transport operators, including competing companies, both in national and reginal level as well as to/from Europe.
