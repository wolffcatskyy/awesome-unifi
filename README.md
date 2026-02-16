# Awesome UniFi [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome tools, libraries, and resources for UniFi and Ubiquiti networking products.

UniFi is a line of networking hardware and software by Ubiquiti Inc., including wireless access points, switches, routers (Dream Machine series), cameras (Protect), and access control systems. This list collects the best community-created tools to enhance your UniFi experience.

## Contents

- [Official Resources](#official-resources)
- [API Libraries](#api-libraries)
  - [Python](#python)
  - [Node.js / JavaScript](#nodejs--javascript)
  - [Go](#go)
  - [PHP](#php)
  - [.NET / C#](#net--c)
  - [Ruby](#ruby)
  - [Rust](#rust)
- [Controller & Management](#controller--management)
- [Docker Images](#docker-images)
- [Monitoring & Metrics](#monitoring--metrics)
  - [Prometheus & Grafana](#prometheus--grafana)
  - [InfluxDB](#influxdb)
  - [Zabbix](#zabbix)
  - [Other Monitoring](#other-monitoring)
- [Home Automation](#home-automation)
  - [Home Assistant](#home-assistant)
  - [Homebridge / HomeKit](#homebridge--homekit)
  - [Other Platforms](#other-platforms)
- [UniFi Protect](#unifi-protect)
- [UniFi Access](#unifi-access)
- [UniFi Talk](#unifi-talk)
- [Network Automation & IaC](#network-automation--iac)
- [Security Tools](#security-tools)
- [DNS & DDNS](#dns--ddns)
- [VPN & WireGuard](#vpn--wireguard)
- [Backup Tools](#backup-tools)
- [CLI Tools](#cli-tools)
- [Guest Portal & Vouchers](#guest-portal--vouchers)
- [Dream Machine Utilities](#dream-machine-utilities)
- [EdgeRouter / EdgeOS](#edgerouter--edgeos)
- [MCP Servers](#mcp-servers)
- [Guides & Documentation](#guides--documentation)
- [Other Tools](#other-tools)

---

## Official Resources

- [Ubiquiti Community](https://community.ui.com/) - Official community forums
- [UniFi Design Center](https://design.ui.com/) - Official network design tool
- [UniFi Downloads](https://ui.com/download/releases/network-server) - Official software downloads
- [UniFi Help Center](https://help.ui.com/) - Official documentation

## API Libraries

### Python

- [Art-of-WiFi/UniFi-API-client](https://github.com/Art-of-WiFi/UniFi-API-client) - A PHP API client class to interact with Ubiquiti's UniFi Controller API (1.3k stars)
- [unpoller/unifi](https://github.com/unpoller/unifi) - Go Library (w/ structures) to grab data from a Ubiquiti UniFi Controller (139 stars)
- [ubiquiti-community/py-unifi](https://github.com/ubiquiti-community/py-unifi) - Python Unifi API Client (18 stars)
- [calmh/unifi-api](https://github.com/calmh/unifi-api) - An API towards the Ubiquity Networks UniFi controller (335 stars) [Unmaintained]
- [tnware/unifi-controller-api](https://github.com/tnware/unifi-controller-api) - A Python client library for interacting with Ubiquiti UniFi Network Controllers (12 stars)
- [delian/pythonUnifiAPI](https://github.com/delian/pythonUnifiAPI) - Python3 port of UniFi-API-Browser API with small extensions (14 stars)

### Node.js / JavaScript

- [jens-maus/node-unifi](https://github.com/jens-maus/node-unifi) - NodeJS class for querying/controlling a UniFi-Controller (UDM-Pro, UDM-SE, UDM, UDR, UDW, CloudKey) (156 stars)
- [delian/node-unifiapi](https://github.com/delian/node-unifiapi) - UniFi API ported to Node.JS (51 stars)
- [thib3113/unifi-client](https://github.com/thib3113/unifi-client) - NodeJs client for Unifi products (44 stars)

### Go

- [paultyng/go-unifi](https://github.com/paultyng/go-unifi) - Unifi Controller API SDK for Go (188 stars)
- [unpoller/unifi](https://github.com/unpoller/unifi) - Go Library to grab data from a Ubiquiti UniFi Controller (139 stars)
- [jsumners/udm-pro-api-client](https://github.com/jsumners/udm-pro-api-client) - A Go library and CLI tool for interacting with the Ubiquiti UDM Pro gateway device (2 stars)
- [ClifHouck/unified](https://github.com/ClifHouck/unified) - An Unofficial UniFi Network & Protect API Client & CLI, written in Golang (14 stars)

### PHP

- [Art-of-WiFi/UniFi-API-client](https://github.com/Art-of-WiFi/UniFi-API-client) - A PHP API client class to interact with Ubiquiti's UniFi Controller API (1.3k stars)
- [jorisvandesande/unifi-api-client](https://github.com/jorisvandesande/unifi-api-client) - Unifi API Client can be used to connect to the API of your Ubiquiti Unifi Controller (21 stars)

### .NET / C#

- [KoenZomers/UniFiApi](https://github.com/KoenZomers/UniFiApi) - API in .NET 9 to fetch data from an on premises Ubiquiti UniFi Controller (75 stars)
- [schwoi/UnifiClient](https://github.com/schwoi/UnifiClient) - .NET Standard wrapper library for the Ubiquiti Unifi Controller (19 stars)
- [dotMorten/UnifiClient](https://github.com/dotMorten/UnifiClient) - A .NET Library for the Ubiquity Unifi REST and Websocket APIs (14 stars)

### Ruby

- [hculap/unifi-api](https://github.com/hculap/unifi-api) - A rewrite of calmh/unifi-api in Ruby (13 stars)

### Rust

- [CallumTeesdale/unifi-rs](https://github.com/CallumTeesdale/unifi-rs) - Unifi api client (5 stars)
- [fedibtc/unifi-client](https://github.com/fedibtc/unifi-client) - A Rust client library for the Ubiquiti UniFi Controller API (3 stars)

## Controller & Management

- [Art-of-WiFi/UniFi-API-browser](https://github.com/Art-of-WiFi/UniFi-API-browser) - Tool to browse data exposed by Ubiquiti's UniFi Controller API (1.2k stars)
- [unifi-utilities/unifios-utilities](https://github.com/unifi-utilities/unifios-utilities) - Enhancing Your UniFi Experience - collection of utilities for UniFi OS (4.3k stars)
- [unofficial-unifi/unifi-pfsense](https://github.com/unofficial-unifi/unifi-pfsense) - A script that installs the UniFi Controller software on pfSense and other FreeBSD systems (776 stars)
- [stevejenkins/unifi-linux-utils](https://github.com/stevejenkins/unifi-linux-utils) - Helpful Linux/Unix scripts for admins of Ubiquiti UniFi wireless products (718 stars)
- [Ozark-Connect/NetworkOptimizer](https://github.com/Ozark-Connect/NetworkOptimizer) - Self-hosted performance optimization and security audit tool for UniFi Networks (470 stars)
- [Crosstalk-Solutions/unifi-toolkit](https://github.com/Crosstalk-Solutions/unifi-toolkit) - A suite of tools for UniFi network management (147 stars)
- [veteranbv/unifi-client-updater](https://github.com/veteranbv/unifi-client-updater) - UniFi client updater tool (47 stars)
- [scyto/docker-UnifiBrowser](https://github.com/scyto/docker-UnifiBrowser) - Docker for UniFi API Browser (41 stars)
- [ZSamuels28/UnifiClientCheck-Docker](https://github.com/ZSamuels28/UnifiClientCheck-Docker) - Monitor UniFi networks for new devices with Telegram or Ntfy alerts (41 stars)

## Docker Images

- [jacobalberty/unifi-docker](https://github.com/jacobalberty/unifi-docker) - Unifi Docker files (2.5k stars)
- [linuxserver/docker-unifi-network-application](https://github.com/linuxserver/docker-unifi-network-application) - LinuxServer.io Docker image for UniFi Network Application (1.1k stars)
- [goofball222/unifi](https://github.com/goofball222/unifi) - UniFi Docker Container (303 stars)
- [Nico640/docker-unms](https://github.com/Nico640/docker-unms) - All-in-one docker image for Ubiquiti UISP (formerly UNMS) - supports x86_64 and ARM (265 stars)
- [pducharme/UniFi-Video-Controller](https://github.com/pducharme/UniFi-Video-Controller) - Docker for Unifi-Video Controller (200 stars)
- [GiuseppeGalilei/Unifi-Network-Application](https://github.com/GiuseppeGalilei/Unifi-Network-Application) - Easily deploy Unifi Network Application on Docker (192 stars)
- [jcberthon/unifi-docker](https://github.com/jcberthon/unifi-docker) - Unifi Controller Docker image and compose (32 stars)
- [fmdlc/unifi-controller](https://github.com/fmdlc/unifi-controller) - Unifi Network Controller for ARM64 architecture (14 stars)

## Monitoring & Metrics

### Prometheus & Grafana

- [unpoller/unpoller](https://github.com/unpoller/unpoller) - Application: Collect ALL UniFi Controller, Site, Device & Client Data - Export to InfluxDB or Prometheus (2.5k stars)
- [WaterByWind/grafana-dashboards](https://github.com/WaterByWind/grafana-dashboards) - Grafana Dashboards including UniFi (293 stars)
- [mdlayher/unifi_exporter](https://github.com/mdlayher/unifi_exporter) - Prometheus exporter that exposes metrics from a Ubiquiti UniFi Controller and UniFi devices (259 stars)
- [timothystewart6/unpoller-unifi](https://github.com/timothystewart6/unpoller-unifi) - Docker Compose stack for monitoring UniFi networks with UnPoller, Prometheus, and Grafana (95 stars)
- [jessestuart/unifi_exporter](https://github.com/jessestuart/unifi_exporter) - Multiarch images for scraping Prometheus metrics from a Unifi Controller (64 stars)
- [unpoller/dashboards](https://github.com/unpoller/dashboards) - UniFi Poller Grafana Dashboards (37 stars)
- [zygiss/snmp-exporter-unifi](https://github.com/zygiss/snmp-exporter-unifi) - Prometheus SNMP exporter generator & SNMP configs for UniFi access points (23 stars)
- [jorgedlcruz/unifi-grafana](https://github.com/jorgedlcruz/unifi-grafana) - Grafana Dashboard for Unifi Cloud Key Gen2 - Using API to InfluxDB Script (7 stars)

### Zabbix

- [patricegautier/unifiZabbix](https://github.com/patricegautier/unifiZabbix) - Zabbix templates to monitor pretty much all Unifi devices (220 stars)
- [MassimilianoPasquini97/zbx_unifi_network](https://github.com/MassimilianoPasquini97/zbx_unifi_network) - Zabbix Template for Unifi Network (110 stars)
- [MassimilianoPasquini97/zbx_unifi_network_api](https://github.com/MassimilianoPasquini97/zbx_unifi_network_api) - UniFi Network Zabbix Template (20 stars)
- [kko/unifi-zabbix-snmpv3](https://github.com/kko/unifi-zabbix-snmpv3) - UniFi Zabbix SNMPv3 template (8 stars)

### Other Monitoring

- [tusc/ntopng-udm](https://github.com/tusc/ntopng-udm) - ntopng Docker image for the UDM base and UDM pro (172 stars)
- [unifianalyzer/recommender](https://github.com/unifianalyzer/recommender) - Recommends tuning for Unifi access points (8 stars)
- [unpoller/datadogunifi](https://github.com/unpoller/datadogunifi) - UniFi Poller Output Plugin for DataDog (8 stars)

## Home Automation

### Home Assistant

- [briis/unifiprotect](https://github.com/briis/unifiprotect) - Control and monitor your Unifi Protect Cameras from Home Assistant (551 stars)
- [hassio-addons/addon-unifi](https://github.com/hassio-addons/addon-unifi) - UniFi Network Application - Home Assistant Community Add-ons (344 stars)
- [imhotep/hass-unifi-access](https://github.com/imhotep/hass-unifi-access) - Unifi Access Integration for Home Assistant (159 stars)
- [elad-bar/ha-edgeos](https://github.com/elad-bar/ha-edgeos) - Integration with EdgeOS (Ubiquiti) (147 stars)
- [ufozone/ha-unifi-voucher](https://github.com/ufozone/ha-unifi-voucher) - UniFi Hotspot Manager Integration (70 stars)
- [ioBroker.unifi](https://github.com/iobroker-community-adapters/ioBroker.unifi) - ioBroker adapter for UniFi network devices (68 stars)
- [sirkirby/unifi-network-rules](https://github.com/sirkirby/unifi-network-rules) - Manage, backup, and automate your UDM firewall policies in Home Assistant (48 stars)
- [biofects/HA-Unifi-Speedtest](https://github.com/biofects/HA-Unifi-Speedtest) - Real-time speed test monitoring for UniFi networks in Home Assistant (23 stars)
- [patagonaa/homeassistant-unifi-led](https://github.com/patagonaa/homeassistant-unifi-led) - Control UniFi access point LEDs via Home Assistant (17 stars)
- [ruaan-deysel/ha-unifi-insights](https://github.com/ruaan-deysel/ha-unifi-insights) - Comprehensive Home Assistant custom integration for UniFi Network and Protect (13 stars)

### Homebridge / HomeKit

- [hjdhjd/homebridge-unifi-protect](https://github.com/hjdhjd/homebridge-unifi-protect) - Complete HomeKit integration for all UniFi Protect device types with full support for HomeKit Secure Video (1.7k stars)
- [hjdhjd/homebridge-unifi-access](https://github.com/hjdhjd/homebridge-unifi-access) - UniFi Access plugin for HomeKit (Homebridge) (70 stars)
- [DouweM/homebridge-unifi-occupancy](https://github.com/DouweM/homebridge-unifi-occupancy) - Homebridge plugin that adds HomeKit occupancy sensors for selected devices on your UniFi network (45 stars)
- [hjdhjd/homebridge-unifi-network](https://github.com/hjdhjd/homebridge-unifi-network) - UniFi Network plugin for HomeKit (via Homebridge) (18 stars)
- [fuelxc/homebridge-unifi-os](https://github.com/fuelxc/homebridge-unifi-os) - Homebridge Plugin for UnifiOS (7 stars)
- [tickez/homebridge-unifi-guest-occupancy-sensor](https://github.com/tickez/homebridge-unifi-guest-occupancy-sensor) - Homebridge plugin indicating guest presence in a Unifi network (6 stars)
- [HerrOtto/unifi-guest-wifi-qr-code](https://github.com/HerrOtto/unifi-guest-wifi-qr-code) - Dynamic Guest WiFi Password Changer and QR Code Generator (6 stars)
- [davidjbradshaw/homebridge-unifi-guest-wifi](https://github.com/davidjbradshaw/homebridge-unifi-guest-wifi) - Hey Siri, turn on the Guest Wifi (5 stars)

### Other Platforms

- [salanki/unifi-mqtt](https://github.com/salanki/unifi-mqtt) - WLAN Association / Disassociation events from UniFi Controller to MQTT publisher (10 stars)
- [bramstroker/UnifiMqttPublisher](https://github.com/bramstroker/UnifiMqttPublisher) - Publishes Unifi controller and AP statistics to a MQTT broker (7 stars)
- [dcramer/unifi-mqtt](https://github.com/dcramer/unifi-mqtt) - UniFi to MQTT bridge (6 stars)

## UniFi Protect

- [keshavdv/unifi-cam-proxy](https://github.com/keshavdv/unifi-cam-proxy) - Enable non-Ubiquiti cameras to work with Unifi NVR (1.8k stars)
- [hjdhjd/homebridge-unifi-protect](https://github.com/hjdhjd/homebridge-unifi-protect) - Complete HomeKit integration for all UniFi Protect device types (1.7k stars)
- [ep1cman/unifi-protect-backup](https://github.com/ep1cman/unifi-protect-backup) - Python tool to backup unifi event clips in realtime (841 stars)
- [briis/unifiprotect](https://github.com/briis/unifiprotect) - Control and monitor your Unifi Protect Cameras from Home Assistant (551 stars)
- [petergeneric/unifi-protect-remux](https://github.com/petergeneric/unifi-protect-remux) - Converts Ubiquiti's proprietary .ubv files into standard MP4 files (310 stars)
- [yuppity/unifi-video-api](https://github.com/yuppity/unifi-video-api) - Python API for UniFi Video (59 stars)
- [mzac/unifi-video-mqtt](https://github.com/mzac/unifi-video-mqtt) - UniFi Video to MQTT bridge (44 stars)
- [kk7ds/luvs](https://github.com/kk7ds/luvs) - Lightweight Unifi Video Server (42 stars)
- [hjdhjd/unifi-access](https://github.com/hjdhjd/unifi-access) - A nearly complete implementation of the UniFi Access API (40 stars)
- [selfhostedhome/unifi-video-gif-mqtt](https://github.com/selfhostedhome/unifi-video-gif-mqtt) - Watch your UniFi Video directory for new videos, convert to gif and notify over mqtt (20 stars)
- [bluewalk/unifi-udm-protect-mqtt](https://github.com/bluewalk/unifi-udm-protect-mqtt) - A docker container to parse UniFi protect eventlog and publish motion events to MQTT (9 stars)
- [bdraco/pyunifiprotect](https://github.com/bdraco/pyunifiprotect) - Python Wrapper for the Unifi Protect API (2 stars)

## UniFi Access

- [imhotep/hass-unifi-access](https://github.com/imhotep/hass-unifi-access) - Unifi Access Integration for Home Assistant (159 stars)
- [jeffreykog/unifi-inform-protocol](https://github.com/jeffreykog/unifi-inform-protocol) - Information about the reverse engineered inform protocol used in Ubiquiti's UniFi access points (111 stars)
- [hjdhjd/homebridge-unifi-access](https://github.com/hjdhjd/homebridge-unifi-access) - UniFi Access plugin for HomeKit (Homebridge) (70 stars)
- [hjdhjd/unifi-access](https://github.com/hjdhjd/unifi-access) - A nearly complete implementation of the UniFi Access API (40 stars)
- [keithah/unifi-access-airbnb](https://github.com/keithah/unifi-access-airbnb) - Integrates UniFi Access with Airbnb reservations using ICS file or Hostex API (31 stars)
- [matejgordon/unipyAccess](https://github.com/matejgordon/unipyAccess) - Python connector for UniFi Access (21 stars)
- [kleo/unipi](https://github.com/kleo/unipi) - WiFi voucher vending machine leveraging UniFi controller and UniFi access points (16 stars)
- [phamels/unifi_access_unlocker](https://github.com/phamels/unifi_access_unlocker) - Unlock Unifi Access doors using their own API (10 stars)
- [uxico-dev/unifi-access-api](https://github.com/uxico-dev/unifi-access-api) - A PHP API client for the Ubiquiti Unifi Access API (5 stars)

## UniFi Talk

- [Gamer08YT/UniFi-Softphone](https://github.com/Gamer08YT/UniFi-Softphone) - Unofficial UniFi Talk Softphone (4 stars)
- [Gamer08YT/UniFi-Talk-Repo](https://github.com/Gamer08YT/UniFi-Talk-Repo) - Unofficial collection of SIP templates for UniFi Talk (2 stars)

## Network Automation & IaC

- [paultyng/terraform-provider-unifi](https://github.com/paultyng/terraform-provider-unifi) - Terraform provider for Unifi (573 stars)
- [pulumiverse/pulumi-unifi](https://github.com/pulumiverse/pulumi-unifi) - Pulumi provider for Unifi network gear (19 stars)
- [ppouliot/ansible-role-ubnt_platform_mgmt](https://github.com/ppouliot/ansible-role-ubnt_platform_mgmt) - Ansible role for managing UBNT EdgeMAX and UniFI network devices (16 stars)
- [erwanclx/UnifiAnsibleModule](https://github.com/erwanclx/UnifiAnsibleModule) - Unofficial Unifi Ansible Module (3 stars)
- [ferventgeek/unifi-firewall-group-updater](https://github.com/ferventgeek/unifi-firewall-group-updater) - Automate Firewall IP Group management on Unifi Controllers (3 stars)

## Security Tools

- [wolffcatskyy/crowdsec-unifi-bouncer](https://github.com/wolffcatskyy/crowdsec-unifi-bouncer) - Install and persist the official CrowdSec firewall bouncer on UniFi OS devices (15 stars)
- [wolffcatskyy/crowdsec-unifi-parser](https://github.com/wolffcatskyy/crowdsec-unifi-parser) - CrowdSec parsers and iptables LOG rules for UniFi Dream Machines (1 star)
- [LordOfPolls/Unifi-Rampart](https://github.com/LordOfPolls/Unifi-Rampart) - Automated threat intelligence for UniFi firewalls - syncs IP lists from Spamhaus, Firehol, abuse.ch (8 stars)
- [trek-e/unifi-security-report](https://github.com/trek-e/unifi-security-report) - A containerized service that monitors UniFi network logs and delivers plain-English reports (23 stars)
- [puzzlepeaches/Log4jUnifi](https://github.com/puzzlepeaches/Log4jUnifi) - Exploiting CVE-2021-44228 in Unifi Network Application for remote code execution (164 stars)
- [ShrikiSilence/SilenceTheLAN](https://github.com/shrisha/SilenceTheLAN) - iOS app to manage UniFi Firewall policies created for kids' downtime (9 stars)
- [coolcat1575/netwatcher](https://github.com/coolcat1575/netwatcher) - Monitor your network for unknown MAC addresses using data from UniFi (19 stars)

## DNS & DDNS

- [willswire/unifi-ddns](https://github.com/willswire/unifi-ddns) - Cloudflare DDNS (Dynamic DNS) support for UniFi OS (1.2k stars)
- [kashalls/external-dns-unifi-webhook](https://github.com/kashalls/external-dns-unifi-webhook) - External-DNS Webhook to manage UniFi DNS Records (274 stars)
- [evaneaston/udm-host-records](https://github.com/evaneaston/udm-host-records) - Scripts to list, add, update, and remove host records in the Ubiquiti UniFI Dream Machine DNS forwarder (116 stars)
- [wicol/unifi-dns](https://github.com/wicol/unifi-dns) - A dnsmasq being populated by aliases/name overrides made in a UniFi controller (47 stars)
- [ymichel/dnsmasqAdBlockUDM](https://github.com/ymichel/dnsmasqAdBlockUDM) - Dnsmasq based Ad blocking for Unifi equipment (UDM-SE & UDM-PRO) (13 stars)
- [missuo/unifi-cloudflare-ddns](https://github.com/missuo/unifi-cloudflare-ddns) - Cloudflare DDNS for UniFi OS (5 stars)
- [jsumners/udm-dns](https://github.com/jsumners/udm-dns) - A Dnsmasq Docker container that polls a UDM-PRO for a list clients to serve as hostnames (8 stars)
- [pridkett/unifi-dns-scripts](https://github.com/pridkett/unifi-dns-scripts) - Give yourself greater control over outbound DNS on your network (5 stars)

## VPN & WireGuard

- [WireGuard/wireguard-vyatta-ubnt](https://github.com/WireGuard/wireguard-vyatta-ubnt) - WireGuard for Ubiquiti Devices (1.5k stars)
- [SierraSoftworks/tailscale-udm](https://github.com/SierraSoftworks/tailscale-udm) - Run Tailscale on your Unifi Dream Machine (1.4k stars)
- [jamesog/tailscale-edgeos](https://github.com/jamesog/tailscale-edgeos) - Running Tailscale on Ubiquiti EdgeOS (386 stars)
- [tusc/wireguard-kmod](https://github.com/tusc/wireguard-kmod) - WireGuard for UDM series routers (348 stars)
- [mafredri/vyatta-wireguard-installer](https://github.com/mafredri/vyatta-wireguard-installer) - Install, upgrade or remove WireGuard on Ubiquiti hardware (152 stars)
- [vchrizz/ER-wizard-WireGuard](https://github.com/vchrizz/ER-wizard-WireGuard) - WireGuard Wizard for Ubiquiti EdgeMAX Devices (108 stars)
- [evie-lau/Unifi-gateway-wpa-supplicant](https://github.com/evie-lau/Unifi-gateway-wpa-supplicant) - Setup wpa_supplicant on Unifi Gateways to bypass ATT modem (87 stars)
- [gridironsolutions/unifios-tailscale](https://github.com/gridironsolutions/unifios-tailscale) - Run Tailscale natively on Unifi UDM-Pro Dream Machine (8 stars)

## Backup Tools

- [zhangyoufu/unifi-backup-decrypt](https://github.com/zhangyoufu/unifi-backup-decrypt) - Decrypt UniFi Network Application backup (.unf <=> .zip) (234 stars)
- [psitem/edgerouter-backup](https://github.com/psitem/edgerouter-backup) - EdgeRouter to git repo backup scripts (77 stars)

## CLI Tools

- [57/unifidash](https://github.com/57/unifidash) - UniFi CLI leveraging private gateway APIs for network telemetry, DPI, and topology (32 stars)
- [xezpeleta/unifi-cli](https://github.com/xezpeleta/unifi-cli) - Unifi CLI tool (3 stars)
- [ClifHouck/unified](https://github.com/ClifHouck/unified) - An Unofficial UniFi Network & Protect API Client & CLI (14 stars)

## Guest Portal & Vouchers

- [glenndehaan/unifi-voucher-site](https://github.com/glenndehaan/unifi-voucher-site) - UniFi Voucher Site is a web-based platform for generating and managing UniFi network guest vouchers (260 stars)
- [PaintSplasher/unifi-voucher-service](https://github.com/PaintSplasher/unifi-voucher-service) - Simple one-click voucher printing for guests without UniFi Controller access (108 stars)
- [DJM0/unifi-voucher-generator](https://github.com/DJM0/unifi-voucher-generator) - Generates UniFi Hotspot vouchers using the UniFi controller API ready for printing (91 stars)
- [etiennecollin/unifi-voucher-manager](https://github.com/etiennecollin/unifi-voucher-manager) - A touch-friendly and secure interface for streamlined creation and management of guest Wi-Fi vouchers (67 stars)
- [Carlgo11/guest-portal](https://github.com/Carlgo11/guest-portal) - External UniFi guest portal (13 stars)
- [seanmavley/unifi-guest-bundle-check](https://github.com/seanmavley/unifi-guest-bundle-check) - Let Unifi Guests check voucher data bundle left (10 stars)
- [emanuelepaiano/jespresso-lite](https://github.com/emanuelepaiano/jespresso-lite) - Espresso Ubiquiti Unifi Guest Portal written in Java / Typescript (8 stars)
- [seanmavley/unifi-voucher-payment-server](https://github.com/seanmavley/unifi-voucher-payment-server) - Unifi Voucher Payment Server (7 stars)
- [batesta/whoshere](https://github.com/batesta/whoshere) - Who's Here? - An automatic "In/Out" board for UniFi networks (22 stars)

## Dream Machine Utilities

- [unifi-utilities/unifios-utilities](https://github.com/unifi-utilities/unifios-utilities) - Enhancing Your UniFi Experience - utilities for UniFi OS (4.3k stars)
- [kchristensen/udm-le](https://github.com/kchristensen/udm-le) - Let's Encrypt support for Ubiquiti UniFi OS (754 stars)
- [fabianishere/udm-iptv](https://github.com/fabianishere/udm-iptv) - Helper tool for configuring routed IPTV on the UniFi Dream Machine (Pro) (583 stars)
- [fabianishere/udm-kernel-tools](https://github.com/fabianishere/udm-kernel-tools) - Tools for bootstrapping custom kernels on the UniFi Dream Machine (333 stars)
- [iceteaSA/ucg-max-fan-control](https://github.com/iceteaSA/ucg-max-fan-control) - UXG-Max/Fibre Dynamic Fan Control (186 stars)
- [alxwolf/ubios-cert](https://github.com/alxwolf/ubios-cert) - Manage SSL / TLS certificates with acme.sh for Ubiquiti UbiOS firmwares (182 stars)
- [fabianishere/udm-kernel](https://github.com/fabianishere/udm-kernel) - Custom Linux kernels for the UniFi Dream Machine (136 stars)
- [renedis/ubnt-auto-fan-speed](https://github.com/renedis/ubnt-auto-fan-speed) - Automatic fan speed setting on UDM-PRO 1.8.5+ firmware (110 stars)
- [TobyAnscombe/udm-setup](https://github.com/TobyAnscombe/udm-setup) - Simple readme for setting up IoT and VLANS on the Unifi Dream Machine (84 stars)
- [davidjenni/udm-pro-network](https://github.com/davidjenni/udm-pro-network) - Unifi UDM-Pro prosumer network configuration (80 stars)
- [cdchris12/UDM-DNS-Fix](https://github.com/cdchris12/UDM-DNS-Fix) - A simple script to provide basic DHCP hostname resolution in the latest UniFi Dream Machine Pro firmware (76 stars)
- [blackjid/inadyn-cloudflare](https://github.com/blackjid/inadyn-cloudflare) - Cloudflare Dynamic DNS backend for Inadyn - for use with Unifi Dream Machine / Pro (67 stars)
- [scyto/multicast-relay](https://github.com/scyto/multicast-relay) - multicast-relay docker for UniFi Dream Machines (62 stars)
- [IngmarStein/unifi-sonos-doc](https://github.com/IngmarStein/unifi-sonos-doc) - How to configure your UniFi network for Sonos (488 stars)
- [esmith443/Verizon-ONT-Bypass](https://github.com/esmith443/Verizon-ONT-Bypass) - Unifi UDM Pro Iszo XPON UNO Verizon FiOS (44 stars)
- [ddominet/UDMPRO-samba](https://github.com/ddominet/UDMPRO-samba) - UDM-PRO drive bay as a network drive (33 stars)
- [dlk3/udm-hacks](https://github.com/dlk3/udm-hacks) - Hacks for Unifi Dream Machine (UDM) Pro (29 stars)
- [kalenarndt/udmp-jumbo-frames](https://github.com/kalenarndt/udmp-jumbo-frames) - Shell script to configure and monitor jumbo frame configuration on the UDM Pro (24 stars)
- [xpherism/udm-proxy](https://github.com/xpherism/udm-proxy) - Caddy proxy for Ubiquiti UDM Pro (20 stars)
- [whi-tw/macvlan-unifios](https://github.com/whi-tw/macvlan-unifios) - macvlan kernel module for UniFi OS devices (20 stars)
- [johnstonjs/unifios-utils](https://github.com/johnstonjs/unifios-utils) - UniFi OS Utilities (14 stars)

## EdgeRouter / EdgeOS

- [jaysoffian/eap_proxy](https://github.com/jaysoffian/eap_proxy) - Proxy EAP packets between interfaces on Linux devices such as the Ubiquiti Networks EdgeRouter and UniFi Security Gateway (594 stars)
- [j-c-m/ubnt-letsencrypt](https://github.com/j-c-m/ubnt-letsencrypt) - Let's Encrypt setup instructions for Ubiquiti EdgeRouter (482 stars)
- [britannic/blacklist](https://github.com/britannic/blacklist) - Blacklist and Adware Blocking for the Ubiquiti EdgeMax Router (537 stars)
- [WaterByWind/edgeos-bl-mgmt](https://github.com/WaterByWind/edgeos-bl-mgmt) - Automated updating of EdgeOS firewall network-group to be used as source address blacklist (202 stars)
- [stevejenkins/UBNT-EdgeRouter-Example-Configs](https://github.com/stevejenkins/UBNT-EdgeRouter-Example-Configs) - Example config.boot files for UBNT EdgeRouters with Google, Comcast, and Charter (199 stars)
- [hungnguyenm/edgemax-acme](https://github.com/hungnguyenm/edgemax-acme) - Let's Encrypt setup instructions for Ubiquiti EdgeRouter using DNS-01 (156 stars)
- [photinus/ubnt-letsencrypt](https://github.com/photinus/ubnt-letsencrypt) - Let's Encrypt setup instructions for Ubiquiti Edgerouter Lite (87 stars)
- [whiskerz007/ubnt_get_wireguard](https://github.com/whiskerz007/ubnt_get_wireguard) - Get WireGuard on Ubiquiti devices (68 stars)
- [brianredbeard/edgeos_setup](https://github.com/brianredbeard/edgeos_setup) - Sensible defaults for EdgeOS based routers (67 stars)
- [Genghis1227/guide_eap_proxy](https://github.com/Genghis1227/guide_eap_proxy) - Instructions for AT&T bypass using EdgeRouter Lite (60 stars)
- [Matthew1471/EdgeOS-API](https://github.com/Matthew1471/EdgeOS-API) - An API wrapper for Ubiquiti EdgeOS operating system (52 stars)
- [darkgrue/Ubiquiti-DNSCrypt-Proxy-2-Configuration-Scripts](https://github.com/darkgrue/Ubiquiti-DNSCrypt-Proxy-2-Configuration-Scripts) - Support scripts for DNSCrypt-Proxy 2, dnsmasq, and DNSSEC on Edgerouter (46 stars)
- [darkxst/erx-migration](https://github.com/darkxst/erx-migration) - Openwrt: Edgerouter X migration scripts for installing or upgrading to Openwrt (45 stars)
- [neilalexander/vyatta-cjdns](https://github.com/neilalexander/vyatta-cjdns) - A cjdns package for Ubiquiti EdgeOS and VyOS (42 stars)
- [amarcu5/EdgeOS-Blacklist](https://github.com/amarcu5/EdgeOS-Blacklist) - Automatically updates IP blacklist for EdgeOS (supports IPv4 & IPv6) (41 stars)

## MCP Servers

- [sirkirby/unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp) - MCP server implementation for the UniFi network application (157 stars)
- [enuno/unifi-mcp-server](https://github.com/enuno/unifi-mcp-server) - An MCP server that leverages official UniFi API (34 stars)
- [bjeans/homelab-mcp](https://github.com/bjeans/homelab-mcp) - MCP servers for managing homelab infrastructure including UniFi networks (13 stars)

## Guides & Documentation

- [IngmarStein/unifi-sonos-doc](https://github.com/IngmarStein/unifi-sonos-doc) - How to configure your UniFi network for Sonos (488 stars)
- [TobyAnscombe/udm-setup](https://github.com/TobyAnscombe/udm-setup) - A simple set of readme's for how to setup IoT and VLANS on the Unifi Dream Machine (84 stars)
- [mzac/unifi-pfsense-tailscale](https://github.com/mzac/unifi-pfsense-tailscale) - Documentation on how to integrate Unifi with pfSense and Tailscale (15 stars)
- [beezly/unifi-apis](https://github.com/beezly/unifi-apis) - UniFi Network and Protect API OpenAPI specifications (11 stars)
- [ubiquiti-community/unifi-api](https://github.com/ubiquiti-community/unifi-api) - OpenAPI Definition for Unifi Controller API (10 stars)
- [MinisculeGirraffe/Tailscale-UDMPro](https://github.com/MinisculeGirraffe/Tailscale-UDMPro) - Guide to running Tailscale on a UDM(Pro) (21 stars)

## Other Tools

- [Unifi-Tools/UFiber.Configurator](https://github.com/Unifi-Tools/UFiber.Configurator) - UFiber Configuration Tool (207 stars)
- [sowbug/mkeosimg](https://github.com/sowbug/mkeosimg) - Make a Ubiquiti EdgeOS image from a system tarball (195 stars)
- [WhiskeyTang0F0xtr0t/unifi](https://github.com/WhiskeyTang0F0xtr0t/unifi) - Random stuff for unifi devices (173 stars)
- [carverauto/serviceradar](https://github.com/carverauto/serviceradar) - Zero-trust Opensource Network Management and Observability Platform (799 stars)
- [jollyjinx/unifi2mqtt](https://github.com/jollyjinx/unifi2mqtt) - Use Ubiquiti Unifi API to get connect devices and clients information to mqtt (7 stars)
- [merlijntishauser/unifi-network-maps](https://github.com/merlijntishauser/unifi-network-maps) - Creates markdown/mermaid network maps using the unifi api (3 stars)

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, the authors have waived all copyright and related or neighboring rights to this work.
