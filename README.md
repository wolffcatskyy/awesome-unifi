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
  - [Rust](#rust)
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
- [UniFi Talk](#unifi-talk)
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

- [delian/node-unifiapi](https://github.com/delian/node-unifiapi) - UniFi API ported to Node.js.
- [jens-maus/node-unifi](https://github.com/jens-maus/node-unifi) - Node.js class for querying and controlling UniFi Controllers across all hardware platforms.
- [thib3113/unifi-client](https://github.com/thib3113/unifi-client) - Node.js client for UniFi products.

### Go

- [ClifHouck/unified](https://github.com/ClifHouck/unified) - Unofficial UniFi Network and Protect API client and CLI written in Go.
- [jsumners/udm-pro-api-client](https://github.com/jsumners/udm-pro-api-client) - Go library and CLI tool for interacting with the Ubiquiti UDM Pro.
- [paultyng/go-unifi](https://github.com/paultyng/go-unifi) - UniFi Controller API SDK for Go.
- [unpoller/unifi](https://github.com/unpoller/unifi) - Go library to grab data from a Ubiquiti UniFi Controller (companion library used by UnPoller).

### PHP

- [Art-of-WiFi/UniFi-API-client](https://github.com/Art-of-WiFi/UniFi-API-client) - PHP API client class to interact with Ubiquiti's UniFi Controller API.
- [jorisvandesande/unifi-api-client](https://github.com/jorisvandesande/unifi-api-client) - UniFi API Client can be used to connect to the API of your Ubiquiti UniFi Controller.

### .NET / C#

- [dotMorten/UnifiClient](https://github.com/dotMorten/UnifiClient) - .NET library for the Ubiquiti UniFi REST and WebSocket APIs.
- [KoenZomers/UniFiApi](https://github.com/KoenZomers/UniFiApi) - API in .NET 9 to fetch data from an on premises Ubiquiti UniFi Controller.
- [schwoi/UnifiClient](https://github.com/schwoi/UnifiClient) - .NET Standard wrapper library for the Ubiquiti UniFi Controller.

### Ruby

- [hculap/unifi-api](https://github.com/hculap/unifi-api) - Ruby client for the UniFi Controller API.

### Rust

- [CallumTeesdale/unifi-rs](https://github.com/CallumTeesdale/unifi-rs) - Rust client for the UniFi Controller API.
- [fedibtc/unifi-client](https://github.com/fedibtc/unifi-client) - Rust client library for the Ubiquiti UniFi Controller API.

## Controller & Management

- [57/unifidash](https://github.com/57/unifidash) - CLI leveraging private gateway APIs for network telemetry, DPI, and topology.
- [Art-of-WiFi/UniFi-API-browser](https://github.com/Art-of-WiFi/UniFi-API-browser) - Tool to browse data exposed by Ubiquiti's UniFi Controller API.
- [Crosstalk-Solutions/unifi-toolkit](https://github.com/Crosstalk-Solutions/unifi-toolkit) - Suite of tools for UniFi network management.
- [merlijntishauser/unifi-network-maps](https://github.com/merlijntishauser/unifi-network-maps) - Creates markdown/mermaid network maps using the UniFi API.
- [Ozark-Connect/NetworkOptimizer](https://github.com/Ozark-Connect/NetworkOptimizer) - Self-hosted performance optimization and security audit tool for UniFi Networks.
- [scyto/docker-UnifiBrowser](https://github.com/scyto/docker-UnifiBrowser) - Dockerized version of the UniFi API Browser.
- [stevejenkins/unifi-linux-utils](https://github.com/stevejenkins/unifi-linux-utils) - Helpful Linux/Unix scripts for admins of Ubiquiti UniFi wireless products.
- [Unifi-Tools/UFiber.Configurator](https://github.com/Unifi-Tools/UFiber.Configurator) - Configuration tool for managing and provisioning Ubiquiti UFiber GPON devices.
- [unifi-utilities/unifios-utilities](https://github.com/unifi-utilities/unifios-utilities) - Community collection of utilities and enhancements for UniFi OS.
- [unofficial-unifi/unifi-pfsense](https://github.com/unofficial-unifi/unifi-pfsense) - Install the UniFi Controller software on pfSense and other FreeBSD systems.
- [veteranbv/unifi-client-updater](https://github.com/veteranbv/unifi-client-updater) - Bulk update client names and metadata across UniFi sites.
- [ZSamuels28/UnifiClientCheck-Docker](https://github.com/ZSamuels28/UnifiClientCheck-Docker) - Monitor UniFi networks for new devices with Telegram or Ntfy alerts.

## Docker Images

- [fmdlc/unifi-controller](https://github.com/fmdlc/unifi-controller) - UniFi Network Controller for ARM64 architecture.
- [GiuseppeGalilei/Unifi-Network-Application](https://github.com/GiuseppeGalilei/Unifi-Network-Application) - Easily deploy UniFi Network Application on Docker.
- [goofball222/unifi](https://github.com/goofball222/unifi) - UniFi Docker Container.
- [jacobalberty/unifi-docker](https://github.com/jacobalberty/unifi-docker) - UniFi Docker files.
- [jcberthon/unifi-docker](https://github.com/jcberthon/unifi-docker) - UniFi Controller Docker image and compose.
- [linuxserver/docker-unifi-network-application](https://github.com/linuxserver/docker-unifi-network-application) - LinuxServer.io Docker image for UniFi Network Application.
- [Nico640/docker-unms](https://github.com/Nico640/docker-unms) - All-in-one Docker image for Ubiquiti UISP (formerly UNMS) - supports x86_64 and ARM.

## Monitoring & Metrics

### Prometheus & Grafana

- [jorgedlcruz/unifi-grafana](https://github.com/jorgedlcruz/unifi-grafana) - Grafana dashboard for UniFi Cloud Key Gen2 using the API to InfluxDB pipeline.
- [timothystewart6/unpoller-unifi](https://github.com/timothystewart6/unpoller-unifi) - Ready-to-run Docker Compose stack for monitoring UniFi networks with UnPoller, Prometheus, and Grafana (third-party deployment stack).
- [unpoller/dashboards](https://github.com/unpoller/dashboards) - Pre-built Grafana dashboards for visualizing UnPoller data (companion dashboards).
- [unpoller/unpoller](https://github.com/unpoller/unpoller) - Collect all UniFi Controller, site, device, and client data and export to InfluxDB or Prometheus.
- [WaterByWind/grafana-dashboards](https://github.com/WaterByWind/grafana-dashboards) - Grafana Dashboards including UniFi.
- [zygiss/snmp-exporter-unifi](https://github.com/zygiss/snmp-exporter-unifi) - Prometheus SNMP exporter generator and SNMP configs for UniFi access points.

### Zabbix

- [kko/unifi-zabbix-snmpv3](https://github.com/kko/unifi-zabbix-snmpv3) - UniFi Zabbix SNMPv3 template.
- [MassimilianoPasquini97/zbx_unifi_network](https://github.com/MassimilianoPasquini97/zbx_unifi_network) - Zabbix Template for UniFi Network.
- [MassimilianoPasquini97/zbx_unifi_network_api](https://github.com/MassimilianoPasquini97/zbx_unifi_network_api) - UniFi Network Zabbix Template.
- [patricegautier/unifiZabbix](https://github.com/patricegautier/unifiZabbix) - Comprehensive Zabbix templates covering all UniFi device types.

### Other Monitoring

- [carverauto/serviceradar](https://github.com/carverauto/serviceradar) - Zero-trust open-source network management and observability platform with UniFi support.
- [tusc/ntopng-udm](https://github.com/tusc/ntopng-udm) - Ntopng Docker image for the UDM base and UDM pro.
- [unpoller/datadogunifi](https://github.com/unpoller/datadogunifi) - Sends UnPoller-collected UniFi metrics to DataDog (output plugin).

## Home Automation

### Home Assistant

- [biofects/HA-Unifi-Speedtest](https://github.com/biofects/HA-Unifi-Speedtest) - Real-time speed test monitoring for UniFi networks in Home Assistant.
- [briis/unifiprotect](https://github.com/briis/unifiprotect) - Control and monitor your UniFi Protect Cameras from Home Assistant.
- [elad-bar/ha-edgeos](https://github.com/elad-bar/ha-edgeos) - Home Assistant integration for Ubiquiti EdgeOS routers.
- [hassio-addons/addon-unifi](https://github.com/hassio-addons/addon-unifi) - UniFi Network Application - Home Assistant Community Add-ons.
- [imhotep/hass-unifi-access](https://github.com/imhotep/hass-unifi-access) - UniFi Access Integration for Home Assistant.
- [patagonaa/homeassistant-unifi-led](https://github.com/patagonaa/homeassistant-unifi-led) - Control UniFi access point LEDs via Home Assistant.
- [ruaan-deysel/ha-unifi-insights](https://github.com/ruaan-deysel/ha-unifi-insights) - Comprehensive Home Assistant custom integration for UniFi Network and Protect.
- [sirkirby/unifi-network-rules](https://github.com/sirkirby/unifi-network-rules) - Manage, backup, and automate your UDM firewall policies in Home Assistant.
- [ufozone/ha-unifi-voucher](https://github.com/ufozone/ha-unifi-voucher) - UniFi Hotspot Manager Integration.

### Homebridge / HomeKit

- [davidjbradshaw/homebridge-unifi-guest-wifi](https://github.com/davidjbradshaw/homebridge-unifi-guest-wifi) - Homebridge plugin for controlling UniFi guest Wi-Fi networks via Siri and HomeKit.
- [DouweM/homebridge-unifi-occupancy](https://github.com/DouweM/homebridge-unifi-occupancy) - Homebridge plugin that adds HomeKit occupancy sensors for selected devices on your UniFi network.
- [fuelxc/homebridge-unifi-os](https://github.com/fuelxc/homebridge-unifi-os) - Homebridge Plugin for UniFi OS.
- [HerrOtto/unifi-guest-wifi-qr-code](https://github.com/HerrOtto/unifi-guest-wifi-qr-code) - Dynamic Guest Wi-Fi Password Changer and QR Code Generator.
- [hjdhjd/homebridge-unifi-access](https://github.com/hjdhjd/homebridge-unifi-access) - UniFi Access plugin for HomeKit (Homebridge).
- [hjdhjd/homebridge-unifi-network](https://github.com/hjdhjd/homebridge-unifi-network) - UniFi Network plugin for HomeKit (via Homebridge).
- [hjdhjd/homebridge-unifi-protect](https://github.com/hjdhjd/homebridge-unifi-protect) - Complete HomeKit integration for all UniFi Protect device types with full support for HomeKit Secure Video.
- [tickez/homebridge-unifi-guest-occupancy-sensor](https://github.com/tickez/homebridge-unifi-guest-occupancy-sensor) - Homebridge plugin indicating guest presence in a UniFi network.

### Other Platforms

- [bramstroker/UnifiMqttPublisher](https://github.com/bramstroker/UnifiMqttPublisher) - Publishes UniFi controller and AP statistics to a MQTT broker.
- [dcramer/unifi-mqtt](https://github.com/dcramer/unifi-mqtt) - UniFi to MQTT bridge.
- [ioBroker.unifi](https://github.com/iobroker-community-adapters/ioBroker.unifi) - ioBroker adapter for UniFi network devices.
- [jollyjinx/unifi2mqtt](https://github.com/jollyjinx/unifi2mqtt) - Publish UniFi device and client information to MQTT.
- [salanki/unifi-mqtt](https://github.com/salanki/unifi-mqtt) - WLAN Association / Disassociation events from UniFi Controller to MQTT publisher.

## UniFi Protect

- [bdraco/pyunifiprotect](https://github.com/bdraco/pyunifiprotect) - Python wrapper for the UniFi Protect API, used by the core Home Assistant integration.
- [bluewalk/unifi-udm-protect-mqtt](https://github.com/bluewalk/unifi-udm-protect-mqtt) - Docker container that parses UniFi Protect event logs and publishes motion events to MQTT.
- [ep1cman/unifi-protect-backup](https://github.com/ep1cman/unifi-protect-backup) - Back up UniFi Protect event clips in realtime to local or cloud storage.
- [keshavdv/unifi-cam-proxy](https://github.com/keshavdv/unifi-cam-proxy) - Enable non-Ubiquiti cameras to work with UniFi NVR.
- [petergeneric/unifi-protect-remux](https://github.com/petergeneric/unifi-protect-remux) - Converts Ubiquiti's proprietary .ubv files into standard MP4 files.

## UniFi Access

- [hjdhjd/unifi-access](https://github.com/hjdhjd/unifi-access) - Comprehensive implementation of the UniFi Access API.
- [keithah/unifi-access-airbnb](https://github.com/keithah/unifi-access-airbnb) - Integrates UniFi Access with Airbnb reservations using ICS file or Hostex API.
- [matejgordon/unipyAccess](https://github.com/matejgordon/unipyAccess) - Python connector for UniFi Access.
- [phamels/unifi_access_unlocker](https://github.com/phamels/unifi_access_unlocker) - Unlock UniFi Access doors using their own API.
- [uxico-dev/unifi-access-api](https://github.com/uxico-dev/unifi-access-api) - PHP API client for the Ubiquiti UniFi Access API.

## UniFi Talk

- [Gamer08YT/UniFi-Softphone](https://github.com/Gamer08YT/UniFi-Softphone) - Unofficial UniFi Talk Softphone.
- [Gamer08YT/UniFi-Talk-Repo](https://github.com/Gamer08YT/UniFi-Talk-Repo) - Unofficial collection of SIP templates for UniFi Talk.

## Network Automation & IaC

- [erwanclx/UnifiAnsibleModule](https://github.com/erwanclx/UnifiAnsibleModule) - Unofficial Ansible module for managing UniFi network resources, filling the gap left by the absence of an official Ubiquiti collection.
- [ferventgeek/unifi-firewall-group-updater](https://github.com/ferventgeek/unifi-firewall-group-updater) - Automate Firewall IP Group management on UniFi Controllers.
- [paultyng/terraform-provider-unifi](https://github.com/paultyng/terraform-provider-unifi) - Terraform provider for UniFi.
- [ppouliot/ansible-role-ubnt_platform_mgmt](https://github.com/ppouliot/ansible-role-ubnt_platform_mgmt) - Ansible role for managing UBNT EdgeMAX and UniFi network devices.
- [pulumiverse/pulumi-unifi](https://github.com/pulumiverse/pulumi-unifi) - Pulumi provider for UniFi network gear.

## Security Tools

- [coolcat1575/netwatcher](https://github.com/coolcat1575/netwatcher) - Monitor your network for unknown MAC addresses using data from UniFi.
- [LordOfPolls/Unifi-Rampart](https://github.com/LordOfPolls/Unifi-Rampart) - Automated threat intelligence for UniFi firewalls - syncs IP lists from Spamhaus, Firehol, abuse.ch.
- [shrisha/SilenceTheLAN](https://github.com/shrisha/SilenceTheLAN) - iOS app to manage UniFi Firewall policies created for kids' downtime.
- [trek-e/unifi-security-report](https://github.com/trek-e/unifi-security-report) - Containerized service that monitors UniFi network logs and delivers plain-English reports.
- [wolffcatskyy/crowdsec-unifi-bouncer](https://github.com/wolffcatskyy/crowdsec-unifi-bouncer) - Install and persist the official CrowdSec firewall bouncer on UniFi OS devices.
- [wolffcatskyy/crowdsec-unifi-parser](https://github.com/wolffcatskyy/crowdsec-unifi-parser) - CrowdSec parsers and iptables LOG rules for UniFi Dream Machines.

## DNS & DDNS

- [evaneaston/udm-host-records](https://github.com/evaneaston/udm-host-records) - Scripts to list, add, update, and remove host records in the Ubiquiti UniFi Dream Machine DNS forwarder.
- [jsumners/udm-dns](https://github.com/jsumners/udm-dns) - Dnsmasq Docker container that polls a UDM Pro for client hostnames.
- [kashalls/external-dns-unifi-webhook](https://github.com/kashalls/external-dns-unifi-webhook) - External-DNS Webhook to manage UniFi DNS Records.
- [missuo/unifi-cloudflare-ddns](https://github.com/missuo/unifi-cloudflare-ddns) - Cloudflare DDNS for UniFi OS.
- [pridkett/unifi-dns-scripts](https://github.com/pridkett/unifi-dns-scripts) - Scripts for greater control over outbound DNS on UniFi networks.
- [wicol/unifi-dns](https://github.com/wicol/unifi-dns) - Dnsmasq populated by aliases and name overrides from a UniFi Controller.
- [willswire/unifi-ddns](https://github.com/willswire/unifi-ddns) - Cloudflare DDNS (Dynamic DNS) support for UniFi OS.
- [ymichel/dnsmasqAdBlockUDM](https://github.com/ymichel/dnsmasqAdBlockUDM) - Dnsmasq based Ad blocking for UniFi equipment (UDM-SE and UDM-PRO).

## VPN & WireGuard

- [evie-lau/Unifi-gateway-wpa-supplicant](https://github.com/evie-lau/Unifi-gateway-wpa-supplicant) - Set up wpa_supplicant on UniFi Gateways to bypass the AT&T modem.
- [gridironsolutions/unifios-tailscale](https://github.com/gridironsolutions/unifios-tailscale) - Run Tailscale natively on UniFi UDM-Pro Dream Machine.
- [jamesog/tailscale-edgeos](https://github.com/jamesog/tailscale-edgeos) - Running Tailscale on Ubiquiti EdgeOS.
- [mafredri/vyatta-wireguard-installer](https://github.com/mafredri/vyatta-wireguard-installer) - Install, upgrade or remove WireGuard on Ubiquiti hardware.
- [SierraSoftworks/tailscale-udm](https://github.com/SierraSoftworks/tailscale-udm) - Run Tailscale on your UniFi Dream Machine.
- [tusc/wireguard-kmod](https://github.com/tusc/wireguard-kmod) - WireGuard for UDM series routers.
- [vchrizz/ER-wizard-WireGuard](https://github.com/vchrizz/ER-wizard-WireGuard) - WireGuard Wizard for Ubiquiti EdgeMAX Devices.
- [WireGuard/wireguard-vyatta-ubnt](https://github.com/WireGuard/wireguard-vyatta-ubnt) - WireGuard for Ubiquiti Devices.

## Backup Tools

- [psitem/edgerouter-backup](https://github.com/psitem/edgerouter-backup) - EdgeRouter to Git repo backup scripts.
- [zhangyoufu/unifi-backup-decrypt](https://github.com/zhangyoufu/unifi-backup-decrypt) - Decrypt UniFi Network Application backup (.unf to .zip).

## Guest Portal & Vouchers

- [batesta/whoshere](https://github.com/batesta/whoshere) - Automatic presence board showing who is on or off the UniFi network.
- [Carlgo11/guest-portal](https://github.com/Carlgo11/guest-portal) - External UniFi guest portal.
- [DJM0/unifi-voucher-generator](https://github.com/DJM0/unifi-voucher-generator) - Generate printable UniFi Hotspot vouchers via the Controller API.
- [emanuelepaiano/jespresso-lite](https://github.com/emanuelepaiano/jespresso-lite) - UniFi guest portal written in Java and TypeScript.
- [etiennecollin/unifi-voucher-manager](https://github.com/etiennecollin/unifi-voucher-manager) - Touch-friendly interface for creating and managing guest Wi-Fi vouchers.
- [glenndehaan/unifi-voucher-site](https://github.com/glenndehaan/unifi-voucher-site) - Web platform for generating and managing UniFi network guest vouchers.
- [kleo/unipi](https://github.com/kleo/unipi) - Wi-Fi voucher vending machine leveraging UniFi Controller and access points.
- [PaintSplasher/unifi-voucher-service](https://github.com/PaintSplasher/unifi-voucher-service) - One-click voucher printing for guests without UniFi Controller access.

## Dream Machine Utilities

- [alxwolf/ubios-cert](https://github.com/alxwolf/ubios-cert) - Manage SSL / TLS certificates with acme.sh for Ubiquiti UbiOS firmwares.
- [blackjid/inadyn-cloudflare](https://github.com/blackjid/inadyn-cloudflare) - Cloudflare Dynamic DNS backend for Inadyn - for use with UniFi Dream Machine / Pro.
- [cdchris12/UDM-DNS-Fix](https://github.com/cdchris12/UDM-DNS-Fix) - Script for DHCP hostname resolution on UniFi Dream Machine Pro firmware.
- [davidjenni/udm-pro-network](https://github.com/davidjenni/udm-pro-network) - UniFi UDM-Pro prosumer network configuration.
- [ddominet/UDMPRO-samba](https://github.com/ddominet/UDMPRO-samba) - UDM-PRO drive bay as a network drive.
- [dlk3/udm-hacks](https://github.com/dlk3/udm-hacks) - Collection of scripts and tweaks for the UniFi Dream Machine Pro.
- [esmith443/Verizon-ONT-Bypass](https://github.com/esmith443/Verizon-ONT-Bypass) - Guide for bypassing the Verizon FiOS ONT with an Iszo XPON UNO on a UDM Pro.
- [fabianishere/udm-iptv](https://github.com/fabianishere/udm-iptv) - Helper tool for configuring routed IPTV on the UniFi Dream Machine (Pro).
- [fabianishere/udm-kernel](https://github.com/fabianishere/udm-kernel) - Custom Linux kernels for the UniFi Dream Machine.
- [fabianishere/udm-kernel-tools](https://github.com/fabianishere/udm-kernel-tools) - Tools for bootstrapping custom kernels on the UniFi Dream Machine.
- [iceteaSA/ucg-max-fan-control](https://github.com/iceteaSA/ucg-max-fan-control) - UXG-Max/Fibre Dynamic Fan Control.
- [IngmarStein/unifi-sonos-doc](https://github.com/IngmarStein/unifi-sonos-doc) - How to configure your UniFi network for Sonos.
- [johnstonjs/unifios-utils](https://github.com/johnstonjs/unifios-utils) - Shell utilities for managing services and configurations on UniFi OS.
- [kalenarndt/udmp-jumbo-frames](https://github.com/kalenarndt/udmp-jumbo-frames) - Shell script to configure and monitor jumbo frame configuration on the UDM Pro.
- [kchristensen/udm-le](https://github.com/kchristensen/udm-le) - Let's Encrypt support for Ubiquiti UniFi OS.
- [renedis/ubnt-auto-fan-speed](https://github.com/renedis/ubnt-auto-fan-speed) - Automatic fan speed setting on UDM-PRO 1.8.5+ firmware.
- [scyto/multicast-relay](https://github.com/scyto/multicast-relay) - Multicast-relay Docker for UniFi Dream Machines.
- [TobyAnscombe/udm-setup](https://github.com/TobyAnscombe/udm-setup) - Guide for setting up IoT VLANs on the UniFi Dream Machine.
- [whi-tw/macvlan-unifios](https://github.com/whi-tw/macvlan-unifios) - Macvlan kernel module for UniFi OS devices.
- [xpherism/udm-proxy](https://github.com/xpherism/udm-proxy) - Caddy proxy for Ubiquiti UDM Pro.

## EdgeRouter / EdgeOS

- [amarcu5/EdgeOS-Blacklist](https://github.com/amarcu5/EdgeOS-Blacklist) - Automatically updates IP blacklist for EdgeOS (supports IPv4 and IPv6).
- [brianredbeard/edgeos_setup](https://github.com/brianredbeard/edgeos_setup) - Sensible defaults for EdgeOS based routers.
- [britannic/blacklist](https://github.com/britannic/blacklist) - Blacklist and Adware Blocking for the Ubiquiti EdgeMax Router.
- [darkgrue/Ubiquiti-DNSCrypt-Proxy-2-Configuration-Scripts](https://github.com/darkgrue/Ubiquiti-DNSCrypt-Proxy-2-Configuration-Scripts) - Support scripts for DNSCrypt-Proxy 2, dnsmasq, and DNSSEC on EdgeRouter.
- [darkxst/erx-migration](https://github.com/darkxst/erx-migration) - EdgeRouter X migration scripts for installing or upgrading to OpenWrt.
- [Genghis1227/guide_eap_proxy](https://github.com/Genghis1227/guide_eap_proxy) - Instructions for AT&T bypass using EdgeRouter Lite.
- [hungnguyenm/edgemax-acme](https://github.com/hungnguyenm/edgemax-acme) - Let's Encrypt setup instructions for Ubiquiti EdgeRouter using DNS-01.
- [j-c-m/ubnt-letsencrypt](https://github.com/j-c-m/ubnt-letsencrypt) - Let's Encrypt setup instructions for Ubiquiti EdgeRouter.
- [Matthew1471/EdgeOS-API](https://github.com/Matthew1471/EdgeOS-API) - API wrapper for the Ubiquiti EdgeOS operating system.
- [neilalexander/vyatta-cjdns](https://github.com/neilalexander/vyatta-cjdns) - Mesh networking via cjdns for Ubiquiti EdgeOS and VyOS.
- [sowbug/mkeosimg](https://github.com/sowbug/mkeosimg) - Make a Ubiquiti EdgeOS image from a system tarball.
- [stevejenkins/UBNT-EdgeRouter-Example-Configs](https://github.com/stevejenkins/UBNT-EdgeRouter-Example-Configs) - Example config.boot files for UBNT EdgeRouters with Google, Comcast, and Charter.
- [WaterByWind/edgeos-bl-mgmt](https://github.com/WaterByWind/edgeos-bl-mgmt) - Automated updating of EdgeOS firewall network-group to be used as source address blacklist.
- [whiskerz007/ubnt_get_wireguard](https://github.com/whiskerz007/ubnt_get_wireguard) - Get WireGuard on Ubiquiti devices.

## MCP Servers

- [bjeans/homelab-mcp](https://github.com/bjeans/homelab-mcp) - MCP servers for managing homelab infrastructure including UniFi networks.
- [enuno/unifi-mcp-server](https://github.com/enuno/unifi-mcp-server) - MCP server that leverages the official UniFi API.
- [sirkirby/unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp) - MCP server implementation for the UniFi network application.

## Guides & Documentation

- [beezly/unifi-apis](https://github.com/beezly/unifi-apis) - UniFi Network and Protect API OpenAPI specifications.
- [jeffreykog/unifi-inform-protocol](https://github.com/jeffreykog/unifi-inform-protocol) - Reverse-engineered documentation of the inform protocol used by UniFi access points.
- [MinisculeGirraffe/Tailscale-UDMPro](https://github.com/MinisculeGirraffe/Tailscale-UDMPro) - Guide to running Tailscale on a UDM(Pro).
- [mzac/unifi-pfsense-tailscale](https://github.com/mzac/unifi-pfsense-tailscale) - Documentation on how to integrate UniFi with pfSense and Tailscale.
- [ubiquiti-community/unifi-api](https://github.com/ubiquiti-community/unifi-api) - OpenAPI Definition for UniFi Controller API.

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

---

*List curation and project selection by the maintainer. AI tools used for formatting, lint compliance, and alphabetical ordering.*
