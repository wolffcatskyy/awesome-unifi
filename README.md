# Awesome UniFi [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
  <a href="https://ui.com"><img width="400" src="media/logo.svg" alt="Awesome UniFi"></a>
</div>

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
- [Controller & Management](#controller--management)
- [Docker Images](#docker-images)
- [Monitoring & Metrics](#monitoring--metrics)
  - [Prometheus & Grafana](#prometheus--grafana)
  - [Zabbix](#zabbix)
  - [Other Monitoring](#other-monitoring)
- [Home Automation](#home-automation)
  - [Home Assistant](#home-assistant)
  - [Homebridge / HomeKit](#homebridge--homekit)
  - [Other Platforms](#other-platforms)
- [UniFi Protect](#unifi-protect)
- [UniFi Access](#unifi-access)
- [Network Automation & IaC](#network-automation--iac)
- [Security Tools](#security-tools)
- [DNS & DDNS](#dns--ddns)
- [VPN & WireGuard](#vpn--wireguard)
- [Backup Tools](#backup-tools)
- [Guest Portal & Vouchers](#guest-portal--vouchers)
- [Dream Machine Utilities](#dream-machine-utilities)
- [EdgeRouter / EdgeOS](#edgerouter--edgeos)
- [MCP Servers](#mcp-servers)
- [Guides & Documentation](#guides--documentation)

---

## Official Resources

- [Ubiquiti Community](https://community.ui.com) - Official community forums.
- [UniFi Design Center](https://design.ui.com) - Official network design tool.
- [UniFi Downloads](https://ui.com/download/releases/network-server) - Official software downloads.
- [UniFi Help Center](https://help.ui.com) - Official documentation.

## API Libraries

### Python

- [tnware/unifi-controller-api](https://github.com/tnware/unifi-controller-api) - Python client library for interacting with Ubiquiti UniFi Network Controllers.
- [ubiquiti-community/py-unifi](https://github.com/ubiquiti-community/py-unifi) - Python UniFi API Client.

### Node.js / JavaScript

- [jens-maus/node-unifi](https://github.com/jens-maus/node-unifi) - Node.js class for querying and controlling UniFi Controllers across all hardware platforms.
- [thib3113/unifi-client](https://github.com/thib3113/unifi-client) - Node.js client for UniFi products.

### Go

- [ClifHouck/unified](https://github.com/ClifHouck/unified) - Unofficial UniFi Network and Protect API client and CLI written in Go.
- [paultyng/go-unifi](https://github.com/paultyng/go-unifi) - UniFi Controller API SDK for Go.
- [unpoller/unifi](https://github.com/unpoller/unifi) - Go library to grab data from a Ubiquiti UniFi Controller (companion library used by UnPoller).

### PHP

- [Art-of-WiFi/UniFi-API-client](https://github.com/Art-of-WiFi/UniFi-API-client) - PHP API client class to interact with Ubiquiti's UniFi Controller API.

### .NET / C#

- [dotMorten/UnifiClient](https://github.com/dotMorten/UnifiClient) - .NET library for the Ubiquiti UniFi REST and WebSocket APIs.
- [KoenZomers/UniFiApi](https://github.com/KoenZomers/UniFiApi) - API in .NET 9 to fetch data from an on premises Ubiquiti UniFi Controller.
- [schwoi/UnifiClient](https://github.com/schwoi/UnifiClient) - .NET Standard wrapper library for the Ubiquiti UniFi Controller.

### Ruby

- [hculap/unifi-api](https://github.com/hculap/unifi-api) - Ruby client for the UniFi Controller API.

## Controller & Management

- [57/unifidash](https://github.com/57/unifidash) - CLI leveraging private gateway APIs for network telemetry, DPI, and topology.
- [Art-of-WiFi/UniFi-API-browser](https://github.com/Art-of-WiFi/UniFi-API-browser) - Tool to browse data exposed by Ubiquiti's UniFi Controller API.
- [Crosstalk-Solutions/unifi-toolkit](https://github.com/Crosstalk-Solutions/unifi-toolkit) - Suite of tools for UniFi network management.
- [gitkodak/unifi-map](https://github.com/gitkodak/unifi-map) - Export topology as zoomable SVG, PDF or an editable draw.io diagram, with real device artwork.
- [hyperb1iss/unifly](https://github.com/hyperb1iss/unifly) - Rust CLI and TUI for managing UniFi controllers via dual Integration and Legacy APIs with real-time WebSocket events.
- [Ozark-Connect/NetworkOptimizer](https://github.com/Ozark-Connect/NetworkOptimizer) - Self-hosted performance optimization and security audit tool for UniFi Networks.
- [scyto/docker-UnifiBrowser](https://github.com/scyto/docker-UnifiBrowser) - Dockerized version of the UniFi API Browser.
- [stevejenkins/unifi-linux-utils](https://github.com/stevejenkins/unifi-linux-utils) - Helpful Linux/Unix scripts for admins of Ubiquiti UniFi wireless products.
- [Unifi-Tools/UFiber.Configurator](https://github.com/Unifi-Tools/UFiber.Configurator) - Configuration tool for managing and provisioning Ubiquiti UFiber GPON devices.
- [unifi-utilities/unifios-utilities](https://github.com/unifi-utilities/unifios-utilities) - Community collection of utilities and enhancements for UniFi OS.
- [unofficial-unifi/unifi-pfsense](https://github.com/unofficial-unifi/unifi-pfsense) - Install the UniFi Controller software on pfSense and other FreeBSD systems.
- [veteranbv/unifi-client-updater](https://github.com/veteranbv/unifi-client-updater) - Bulk update client names and metadata across UniFi sites.
- [ZSamuels28/UnifiClientCheck-Docker](https://github.com/ZSamuels28/UnifiClientCheck-Docker) - Monitor UniFi networks for new devices with Telegram or Ntfy alerts.

## Docker Images

- [GiuseppeGalilei/Unifi-Network-Application](https://github.com/GiuseppeGalilei/Unifi-Network-Application) - Easily deploy UniFi Network Application on Docker.
- [goofball222/unifi](https://github.com/goofball222/unifi) - UniFi Docker Container.
- [jacobalberty/unifi-docker](https://github.com/jacobalberty/unifi-docker) - UniFi Docker files.
- [jcberthon/unifi-docker](https://github.com/jcberthon/unifi-docker) - UniFi Controller Docker image and compose.
- [linuxserver/docker-unifi-network-application](https://github.com/linuxserver/docker-unifi-network-application) - LinuxServer.io Docker image for UniFi Network Application.
- [Nico640/docker-unms](https://github.com/Nico640/docker-unms) - All-in-one Docker image for Ubiquiti UISP (formerly UNMS) - supports x86_64 and ARM.

## Monitoring & Metrics

### Prometheus & Grafana

- [timothystewart6/unpoller-unifi](https://github.com/timothystewart6/unpoller-unifi) - Ready-to-run Docker Compose stack for monitoring UniFi networks with UnPoller, Prometheus, and Grafana (third-party deployment stack).
- [unpoller/dashboards](https://github.com/unpoller/dashboards) - Pre-built Grafana dashboards for visualizing UnPoller data (companion dashboards).
- [unpoller/unpoller](https://github.com/unpoller/unpoller) - Collect all UniFi Controller, site, device, and client data and export to InfluxDB or Prometheus.
- [zygiss/snmp-exporter-unifi](https://github.com/zygiss/snmp-exporter-unifi) - Prometheus SNMP exporter generator and SNMP configs for UniFi access points.

### Zabbix

- [MassimilianoPasquini97/zbx_unifi_network_api](https://github.com/MassimilianoPasquini97/zbx_unifi_network_api) - UniFi Network Zabbix Template.
- [patricegautier/unifiZabbix](https://github.com/patricegautier/unifiZabbix) - Comprehensive Zabbix templates covering all UniFi device types.

### Other Monitoring

- [carverauto/serviceradar](https://github.com/carverauto/serviceradar) - Zero-trust open-source network management and observability platform with UniFi support.
- [jmasarweh/Unifi-Log-Insights](https://github.com/jmasarweh/Unifi-Log-Insights) - Self-hosted real-time syslog analysis for UniFi gateways with GeoIP enrichment, threat intelligence, and interactive dashboards.

## Home Automation

### Home Assistant

- [biofects/HA-Unifi-Speedtest](https://github.com/biofects/HA-Unifi-Speedtest) - Real-time speed test monitoring for UniFi networks in Home Assistant.
- [elad-bar/ha-edgeos](https://github.com/elad-bar/ha-edgeos) - Home Assistant integration for Ubiquiti EdgeOS routers.
- [hassio-addons/addon-unifi](https://github.com/hassio-addons/addon-unifi) - UniFi Network Application - Home Assistant Community Add-ons.
- [imhotep/hass-unifi-access](https://github.com/imhotep/hass-unifi-access) - UniFi Access Integration for Home Assistant.
- [patagonaa/homeassistant-unifi-led](https://github.com/patagonaa/homeassistant-unifi-led) - Control UniFi access point LEDs via Home Assistant.
- [ruaan-deysel/ha-unifi-insights](https://github.com/ruaan-deysel/ha-unifi-insights) - Comprehensive Home Assistant custom integration for UniFi Network and Protect.
- [sirkirby/unifi-network-rules](https://github.com/sirkirby/unifi-network-rules) - Manage, backup, and automate your UDM firewall policies in Home Assistant.
- [ufozone/ha-unifi-voucher](https://github.com/ufozone/ha-unifi-voucher) - UniFi Hotspot Manager Integration.

### Homebridge / HomeKit

- [hjdhjd/homebridge-unifi-access](https://github.com/hjdhjd/homebridge-unifi-access) - UniFi Access plugin for HomeKit (Homebridge).
- [hjdhjd/homebridge-unifi-protect](https://github.com/hjdhjd/homebridge-unifi-protect) - Complete HomeKit integration for all UniFi Protect device types with full support for HomeKit Secure Video.

### Other Platforms

- [ioBroker.unifi](https://github.com/iobroker-community-adapters/ioBroker.unifi) - ioBroker adapter for UniFi network devices.

## UniFi Protect

- [danielfernau/unifi-protect-video-downloader](https://github.com/danielfernau/unifi-protect-video-downloader) - Download video footage from UniFi Protect locally.
- [ep1cman/unifi-protect-backup](https://github.com/ep1cman/unifi-protect-backup) - Back up UniFi Protect event clips in realtime to local or cloud storage.
- [hjdhjd/unifi-protect](https://github.com/hjdhjd/unifi-protect) - Comprehensive UniFi Protect API implementation in TypeScript.
- [keshavdv/unifi-cam-proxy](https://github.com/keshavdv/unifi-cam-proxy) - Enable non-Ubiquiti cameras to work with UniFi NVR.
- [petergeneric/unifi-protect-remux](https://github.com/petergeneric/unifi-protect-remux) - Converts Ubiquiti's proprietary .ubv files into standard MP4 files.

## UniFi Access

- [hjdhjd/unifi-access](https://github.com/hjdhjd/unifi-access) - Comprehensive implementation of the UniFi Access API.
- [keithah/unifi-access-airbnb](https://github.com/keithah/unifi-access-airbnb) - Integrates UniFi Access with Airbnb reservations using ICS file or Hostex API.
- [matejgordon/unipyAccess](https://github.com/matejgordon/unipyAccess) - Python connector for UniFi Access.
- [phamels/unifi_access_unlocker](https://github.com/phamels/unifi_access_unlocker) - Unlock UniFi Access doors using their own API.

## Network Automation & IaC

- [paultyng/terraform-provider-unifi](https://github.com/paultyng/terraform-provider-unifi) - Terraform provider for UniFi.
- [pulumiverse/pulumi-unifi](https://github.com/pulumiverse/pulumi-unifi) - Pulumi provider for UniFi network gear.

## Security Tools

- [coolcat1575/netwatcher](https://github.com/coolcat1575/netwatcher) - Monitor your network for unknown MAC addresses using data from UniFi.
- [jmasarweh/Unifi-Log-Insights](https://github.com/jmasarweh/Unifi-Log-Insights) - Real-time syslog analysis for UniFi gateways with AbuseIPDB threat scoring, threat maps, and firewall policy management.
- [LordOfPolls/Unifi-Rampart](https://github.com/LordOfPolls/Unifi-Rampart) - Automated threat intelligence for UniFi firewalls - syncs IP lists from Spamhaus, Firehol, abuse.ch.
- [shrisha/SilenceTheLAN](https://github.com/shrisha/SilenceTheLAN) - iOS app to manage UniFi Firewall policies created for kids' downtime.
- [trek-e/unifi-security-report](https://github.com/trek-e/unifi-security-report) - Containerized service that monitors UniFi network logs and delivers plain-English reports.
- [wolffcatskyy/crowdsec-unifi-bouncer](https://github.com/wolffcatskyy/crowdsec-unifi-bouncer) - Install and persist the official CrowdSec firewall bouncer on UniFi OS devices.
- [wolffcatskyy/crowdsec-unifi-parser](https://github.com/wolffcatskyy/crowdsec-unifi-parser) - CrowdSec parsers and iptables LOG rules for UniFi Dream Machines.
- [wolffcatskyy/crowdsec-blocklist-import](https://github.com/wolffcatskyy/crowdsec-blocklist-import) - Import 120k+ IPs from 36 free threat feeds into CrowdSec decisions for UniFi.
- [wolffcatskyy/crowdsec-unifi-suite](https://github.com/wolffcatskyy/crowdsec-unifi-suite) - One-command installer for CrowdSec + UniFi security stack (bouncer + parser + blocklist-import).

## DNS & DDNS

- [kashalls/external-dns-unifi-webhook](https://github.com/kashalls/external-dns-unifi-webhook) - External-DNS Webhook to manage UniFi DNS Records.
- [willswire/unifi-ddns](https://github.com/willswire/unifi-ddns) - Cloudflare DDNS (Dynamic DNS) support for UniFi OS.
- [ymichel/dnsmasqAdBlockUDM](https://github.com/ymichel/dnsmasqAdBlockUDM) - Dnsmasq based Ad blocking for UniFi equipment (UDM-SE and UDM-PRO).

## VPN & WireGuard

- [evie-lau/Unifi-gateway-wpa-supplicant](https://github.com/evie-lau/Unifi-gateway-wpa-supplicant) - Set up wpa_supplicant on UniFi Gateways to bypass the AT&T modem.
- [jamesog/tailscale-edgeos](https://github.com/jamesog/tailscale-edgeos) - Running Tailscale on Ubiquiti EdgeOS.
- [peacey/split-vpn](https://github.com/peacey/split-vpn) - Policy-based split tunnel VPN for UniFi OS gateways.
- [SierraSoftworks/tailscale-udm](https://github.com/SierraSoftworks/tailscale-udm) - Run Tailscale on your UniFi Dream Machine.
- [tusc/wireguard-kmod](https://github.com/tusc/wireguard-kmod) - WireGuard for UDM series routers.
- [vchrizz/ER-wizard-WireGuard](https://github.com/vchrizz/ER-wizard-WireGuard) - WireGuard Wizard for Ubiquiti EdgeMAX Devices.
- [WireGuard/wireguard-vyatta-ubnt](https://github.com/WireGuard/wireguard-vyatta-ubnt) - WireGuard for Ubiquiti Devices.

## Backup Tools

- [psitem/edgerouter-backup](https://github.com/psitem/edgerouter-backup) - EdgeRouter to Git repo backup scripts.
- [zhangyoufu/unifi-backup-decrypt](https://github.com/zhangyoufu/unifi-backup-decrypt) - Decrypt UniFi Network Application backup (.unf to .zip).

## Guest Portal & Vouchers

- [Carlgo11/guest-portal](https://github.com/Carlgo11/guest-portal) - External UniFi guest portal.
- [DJM0/unifi-voucher-generator](https://github.com/DJM0/unifi-voucher-generator) - Generate printable UniFi Hotspot vouchers via the Controller API.
- [etiennecollin/unifi-voucher-manager](https://github.com/etiennecollin/unifi-voucher-manager) - Touch-friendly interface for creating and managing guest Wi-Fi vouchers.
- [glenndehaan/unifi-voucher-site](https://github.com/glenndehaan/unifi-voucher-site) - Web platform for generating and managing UniFi network guest vouchers.

## Dream Machine Utilities

- [blackjid/inadyn-cloudflare](https://github.com/blackjid/inadyn-cloudflare) - Cloudflare Dynamic DNS backend for Inadyn - for use with UniFi Dream Machine / Pro.
- [cdchris12/UDM-DNS-Fix](https://github.com/cdchris12/UDM-DNS-Fix) - Script for DHCP hostname resolution on UniFi Dream Machine Pro firmware.
- [davidjenni/udm-pro-network](https://github.com/davidjenni/udm-pro-network) - UniFi UDM-Pro prosumer network configuration.
- [dlk3/udm-hacks](https://github.com/dlk3/udm-hacks) - Collection of scripts and tweaks for the UniFi Dream Machine Pro.
- [esmith443/Verizon-ONT-Bypass](https://github.com/esmith443/Verizon-ONT-Bypass) - Guide for bypassing the Verizon FiOS ONT with an Iszo XPON UNO on a UDM Pro.
- [fabianishere/udm-iptv](https://github.com/fabianishere/udm-iptv) - Helper tool for configuring routed IPTV on the UniFi Dream Machine (Pro).
- [fabianishere/udm-kernel](https://github.com/fabianishere/udm-kernel) - Custom Linux kernels for the UniFi Dream Machine.
- [fabianishere/udm-kernel-tools](https://github.com/fabianishere/udm-kernel-tools) - Tools for bootstrapping custom kernels on the UniFi Dream Machine.
- [iceteaSA/ucg-max-fan-control](https://github.com/iceteaSA/ucg-max-fan-control) - UXG-Max/Fibre Dynamic Fan Control.
- [IngmarStein/unifi-sonos-doc](https://github.com/IngmarStein/unifi-sonos-doc) - How to configure your UniFi network for Sonos.
- [johnstonjs/unifios-utils](https://github.com/johnstonjs/unifios-utils) - Shell utilities for managing services and configurations on UniFi OS.
- [kchristensen/udm-le](https://github.com/kchristensen/udm-le) - Let's Encrypt support for Ubiquiti UniFi OS.
- [renedis/ubnt-auto-fan-speed](https://github.com/renedis/ubnt-auto-fan-speed) - Automatic fan speed setting on UDM-PRO 1.8.5+ firmware.
- [scyto/multicast-relay](https://github.com/scyto/multicast-relay) - Multicast-relay Docker for UniFi Dream Machines.
- [TobyAnscombe/udm-setup](https://github.com/TobyAnscombe/udm-setup) - Guide for setting up IoT VLANs on the UniFi Dream Machine.
- [whi-tw/macvlan-unifios](https://github.com/whi-tw/macvlan-unifios) - Macvlan kernel module for UniFi OS devices.
- [xpherism/udm-proxy](https://github.com/xpherism/udm-proxy) - Caddy proxy for Ubiquiti UDM Pro.

## EdgeRouter / EdgeOS

- [britannic/blacklist](https://github.com/britannic/blacklist) - Blacklist and Adware Blocking for the Ubiquiti EdgeMax Router.
- [darkgrue/Ubiquiti-DNSCrypt-Proxy-2-Configuration-Scripts](https://github.com/darkgrue/Ubiquiti-DNSCrypt-Proxy-2-Configuration-Scripts) - Support scripts for DNSCrypt-Proxy 2, dnsmasq, and DNSSEC on EdgeRouter.
- [darkxst/erx-migration](https://github.com/darkxst/erx-migration) - EdgeRouter X migration scripts for installing or upgrading to OpenWrt.
- [Genghis1227/guide_eap_proxy](https://github.com/Genghis1227/guide_eap_proxy) - Instructions for AT&T bypass using EdgeRouter Lite.
- [hungnguyenm/edgemax-acme](https://github.com/hungnguyenm/edgemax-acme) - Let's Encrypt setup instructions for Ubiquiti EdgeRouter using DNS-01.
- [j-c-m/ubnt-letsencrypt](https://github.com/j-c-m/ubnt-letsencrypt) - Let's Encrypt setup instructions for Ubiquiti EdgeRouter.
- [Matthew1471/EdgeOS-API](https://github.com/Matthew1471/EdgeOS-API) - API wrapper for the Ubiquiti EdgeOS operating system.
- [sowbug/mkeosimg](https://github.com/sowbug/mkeosimg) - Make a Ubiquiti EdgeOS image from a system tarball.

## MCP Servers

- [bjeans/homelab-mcp](https://github.com/bjeans/homelab-mcp) - MCP servers for managing homelab infrastructure including UniFi networks.
- [enuno/unifi-mcp-server](https://github.com/enuno/unifi-mcp-server) - MCP server that leverages the official UniFi API.
- [jmasarweh/Unifi-Log-Insights](https://github.com/jmasarweh/Unifi-Log-Insights) - MCP server for querying parsed UniFi firewall logs, threat intelligence, and network analytics.
- [sirkirby/unifi-mcp](https://github.com/sirkirby/unifi-mcp) - MCP server for the UniFi suite including Network, Protect, Access, and Drive.

## Guides & Documentation

- [beezly/unifi-apis](https://github.com/beezly/unifi-apis) - UniFi Network and Protect API OpenAPI specifications.
- [jeffreykog/unifi-inform-protocol](https://github.com/jeffreykog/unifi-inform-protocol) - Reverse-engineered documentation of the inform protocol used by UniFi access points.
- [MinisculeGirraffe/Tailscale-UDMPro](https://github.com/MinisculeGirraffe/Tailscale-UDMPro) - Guide to running Tailscale on a UDM(Pro).
- [mzac/unifi-pfsense-tailscale](https://github.com/mzac/unifi-pfsense-tailscale) - Documentation on how to integrate UniFi with pfSense and Tailscale.
- [ubiquiti-community/unifi-api](https://github.com/ubiquiti-community/unifi-api) - OpenAPI Definition for UniFi Controller API.

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## Footnotes

*List curation and project selection by the maintainer. AI tools used for formatting, lint compliance, and alphabetical ordering.*
