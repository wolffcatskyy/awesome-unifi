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

---

## Official Resources

- [Ubiquiti Community](https://community.ui.com/) - Official community forums.
- [UniFi Design Center](https://design.ui.com/) - Official network design tool.
- [UniFi Downloads](https://ui.com/download/releases/network-server) - Official software downloads.
- [UniFi Help Center](https://help.ui.com/) - Official documentation.

## API Libraries

### Python

- [ubiquiti-community/py-unifi](https://github.com/ubiquiti-community/py-unifi) - Python Unifi API Client.
- [tnware/unifi-controller-api](https://github.com/tnware/unifi-controller-api) - A Python client library for interacting with Ubiquiti UniFi Network Controllers.
- [delian/pythonUnifiAPI](https://github.com/delian/pythonUnifiAPI) - Python3 port of UniFi-API-Browser API with small extensions.

### Node.js / JavaScript

- [jens-maus/node-unifi](https://github.com/jens-maus/node-unifi) - Node.js class for querying/controlling a UniFi-Controller (UDM-Pro, UDM-SE, UDM, UDR, UDW, CloudKey).
- [delian/node-unifiapi](https://github.com/delian/node-unifiapi) - UniFi API ported to Node.js.
- [thib3113/unifi-client](https://github.com/thib3113/unifi-client) - Node.js client for Unifi products.

### Go

- [paultyng/go-unifi](https://github.com/paultyng/go-unifi) - Unifi Controller API SDK for Go.
- [unpoller/unifi](https://github.com/unpoller/unifi) - Go Library to grab data from a Ubiquiti UniFi Controller.
- [jsumners/udm-pro-api-client](https://github.com/jsumners/udm-pro-api-client) - A Go library and CLI tool for interacting with the Ubiquiti UDM Pro gateway device.
- [ClifHouck/unified](https://github.com/ClifHouck/unified) - An Unofficial UniFi Network and Protect API Client and CLI, written in Golang.

### PHP

- [Art-of-WiFi/UniFi-API-client](https://github.com/Art-of-WiFi/UniFi-API-client) - A PHP API client class to interact with Ubiquiti's UniFi Controller API.
- [jorisvandesande/unifi-api-client](https://github.com/jorisvandesande/unifi-api-client) - Unifi API Client can be used to connect to the API of your Ubiquiti Unifi Controller.

### .NET / C#

- [KoenZomers/UniFiApi](https://github.com/KoenZomers/UniFiApi) - API in .NET 9 to fetch data from an on premises Ubiquiti UniFi Controller.
- [schwoi/UnifiClient](https://github.com/schwoi/UnifiClient) - .NET Standard wrapper library for the Ubiquiti Unifi Controller.
- [dotMorten/UnifiClient](https://github.com/dotMorten/UnifiClient) - A .NET Library for the Ubiquity Unifi REST and WebSocket APIs.

### Ruby

- [hculap/unifi-api](https://github.com/hculap/unifi-api) - A rewrite of calmh/unifi-api in Ruby.

### Rust

- [CallumTeesdale/unifi-rs](https://github.com/CallumTeesdale/unifi-rs) - Unifi API client.
- [fedibtc/unifi-client](https://github.com/fedibtc/unifi-client) - A Rust client library for the Ubiquiti UniFi Controller API.

## Controller & Management

- [Art-of-WiFi/UniFi-API-browser](https://github.com/Art-of-WiFi/UniFi-API-browser) - Tool to browse data exposed by Ubiquiti's UniFi Controller API.
- [unifi-utilities/unifios-utilities](https://github.com/unifi-utilities/unifios-utilities) - Enhancing Your UniFi Experience - collection of utilities for UniFi OS.
- [unofficial-unifi/unifi-pfsense](https://github.com/unofficial-unifi/unifi-pfsense) - A script that installs the UniFi Controller software on pfSense and other FreeBSD systems.
- [stevejenkins/unifi-linux-utils](https://github.com/stevejenkins/unifi-linux-utils) - Helpful Linux/Unix scripts for admins of Ubiquiti UniFi wireless products.
- [Ozark-Connect/NetworkOptimizer](https://github.com/Ozark-Connect/NetworkOptimizer) - Self-hosted performance optimization and security audit tool for UniFi Networks.
- [Crosstalk-Solutions/unifi-toolkit](https://github.com/Crosstalk-Solutions/unifi-toolkit) - A suite of tools for UniFi network management.
- [veteranbv/unifi-client-updater](https://github.com/veteranbv/unifi-client-updater) - UniFi client updater tool.
- [scyto/docker-UnifiBrowser](https://github.com/scyto/docker-UnifiBrowser) - Docker for UniFi API Browser.
- [ZSamuels28/UnifiClientCheck-Docker](https://github.com/ZSamuels28/UnifiClientCheck-Docker) - Monitor UniFi networks for new devices with Telegram or Ntfy alerts.
- [Unifi-Tools/UFiber.Configurator](https://github.com/Unifi-Tools/UFiber.Configurator) - UFiber Configuration Tool.
- [merlijntishauser/unifi-network-maps](https://github.com/merlijntishauser/unifi-network-maps) - Creates markdown/mermaid network maps using the UniFi API.

## Docker Images

- [jacobalberty/unifi-docker](https://github.com/jacobalberty/unifi-docker) - Unifi Docker files.
- [linuxserver/docker-unifi-network-application](https://github.com/linuxserver/docker-unifi-network-application) - LinuxServer.io Docker image for UniFi Network Application.
- [goofball222/unifi](https://github.com/goofball222/unifi) - UniFi Docker Container.
- [Nico640/docker-unms](https://github.com/Nico640/docker-unms) - All-in-one Docker image for Ubiquiti UISP (formerly UNMS) - supports x86_64 and ARM.
- [pducharme/UniFi-Video-Controller](https://github.com/pducharme/UniFi-Video-Controller) - Docker for Unifi-Video Controller.
- [GiuseppeGalilei/Unifi-Network-Application](https://github.com/GiuseppeGalilei/Unifi-Network-Application) - Easily deploy Unifi Network Application on Docker.
- [jcberthon/unifi-docker](https://github.com/jcberthon/unifi-docker) - Unifi Controller Docker image and compose.
- [fmdlc/unifi-controller](https://github.com/fmdlc/unifi-controller) - Unifi Network Controller for ARM64 architecture.

## Monitoring & Metrics

### Prometheus & Grafana

- [unpoller/unpoller](https://github.com/unpoller/unpoller) - Application: Collect ALL UniFi Controller, Site, Device and Client Data - Export to InfluxDB or Prometheus.
- [WaterByWind/grafana-dashboards](https://github.com/WaterByWind/grafana-dashboards) - Grafana Dashboards including UniFi.
- [mdlayher/unifi_exporter](https://github.com/mdlayher/unifi_exporter) - Prometheus exporter that exposes metrics from a Ubiquiti UniFi Controller and UniFi devices.
- [timothystewart6/unpoller-unifi](https://github.com/timothystewart6/unpoller-unifi) - Docker Compose stack for monitoring UniFi networks with UnPoller, Prometheus, and Grafana.
- [jessestuart/unifi_exporter](https://github.com/jessestuart/unifi_exporter) - Multiarch images for scraping Prometheus metrics from a Unifi Controller.
- [unpoller/dashboards](https://github.com/unpoller/dashboards) - UniFi Poller Grafana Dashboards.
- [zygiss/snmp-exporter-unifi](https://github.com/zygiss/snmp-exporter-unifi) - Prometheus SNMP exporter generator and SNMP configs for UniFi access points.
- [jorgedlcruz/unifi-grafana](https://github.com/jorgedlcruz/unifi-grafana) - Grafana Dashboard for Unifi Cloud Key Gen2 - Using API to InfluxDB Script.

### Zabbix

- [patricegautier/unifiZabbix](https://github.com/patricegautier/unifiZabbix) - Zabbix templates to monitor pretty much all Unifi devices.
- [MassimilianoPasquini97/zbx_unifi_network](https://github.com/MassimilianoPasquini97/zbx_unifi_network) - Zabbix Template for Unifi Network.
- [MassimilianoPasquini97/zbx_unifi_network_api](https://github.com/MassimilianoPasquini97/zbx_unifi_network_api) - UniFi Network Zabbix Template.
- [kko/unifi-zabbix-snmpv3](https://github.com/kko/unifi-zabbix-snmpv3) - UniFi Zabbix SNMPv3 template.

### Other Monitoring

- [tusc/ntopng-udm](https://github.com/tusc/ntopng-udm) - Ntopng Docker image for the UDM base and UDM pro.
- [unifianalyzer/recommender](https://github.com/unifianalyzer/recommender) - Recommends tuning for Unifi access points.
- [unpoller/datadogunifi](https://github.com/unpoller/datadogunifi) - UniFi Poller Output Plugin for DataDog.
- [carverauto/serviceradar](https://github.com/carverauto/serviceradar) - Zero-trust open-source network management and observability platform with UniFi support.

## Home Automation

### Home Assistant

- [briis/unifiprotect](https://github.com/briis/unifiprotect) - Control and monitor your Unifi Protect Cameras from Home Assistant.
- [hassio-addons/addon-unifi](https://github.com/hassio-addons/addon-unifi) - UniFi Network Application - Home Assistant Community Add-ons.
- [imhotep/hass-unifi-access](https://github.com/imhotep/hass-unifi-access) - Unifi Access Integration for Home Assistant.
- [elad-bar/ha-edgeos](https://github.com/elad-bar/ha-edgeos) - Integration with EdgeOS (Ubiquiti).
- [ufozone/ha-unifi-voucher](https://github.com/ufozone/ha-unifi-voucher) - UniFi Hotspot Manager Integration.
- [ioBroker.unifi](https://github.com/iobroker-community-adapters/ioBroker.unifi) - ioBroker adapter for UniFi network devices.
- [sirkirby/unifi-network-rules](https://github.com/sirkirby/unifi-network-rules) - Manage, backup, and automate your UDM firewall policies in Home Assistant.
- [biofects/HA-Unifi-Speedtest](https://github.com/biofects/HA-Unifi-Speedtest) - Real-time speed test monitoring for UniFi networks in Home Assistant.
- [patagonaa/homeassistant-unifi-led](https://github.com/patagonaa/homeassistant-unifi-led) - Control UniFi access point LEDs via Home Assistant.
- [ruaan-deysel/ha-unifi-insights](https://github.com/ruaan-deysel/ha-unifi-insights) - Comprehensive Home Assistant custom integration for UniFi Network and Protect.

### Homebridge / HomeKit

- [hjdhjd/homebridge-unifi-protect](https://github.com/hjdhjd/homebridge-unifi-protect) - Complete HomeKit integration for all UniFi Protect device types with full support for HomeKit Secure Video.
- [hjdhjd/homebridge-unifi-access](https://github.com/hjdhjd/homebridge-unifi-access) - UniFi Access plugin for HomeKit (Homebridge).
- [DouweM/homebridge-unifi-occupancy](https://github.com/DouweM/homebridge-unifi-occupancy) - Homebridge plugin that adds HomeKit occupancy sensors for selected devices on your UniFi network.
- [hjdhjd/homebridge-unifi-network](https://github.com/hjdhjd/homebridge-unifi-network) - UniFi Network plugin for HomeKit (via Homebridge).
- [fuelxc/homebridge-unifi-os](https://github.com/fuelxc/homebridge-unifi-os) - Homebridge Plugin for UnifiOS.
- [tickez/homebridge-unifi-guest-occupancy-sensor](https://github.com/tickez/homebridge-unifi-guest-occupancy-sensor) - Homebridge plugin indicating guest presence in a Unifi network.
- [HerrOtto/unifi-guest-wifi-qr-code](https://github.com/HerrOtto/unifi-guest-wifi-qr-code) - Dynamic Guest WiFi Password Changer and QR Code Generator.
- [davidjbradshaw/homebridge-unifi-guest-wifi](https://github.com/davidjbradshaw/homebridge-unifi-guest-wifi) - Hey Siri, turn on the Guest Wifi.

### Other Platforms

- [salanki/unifi-mqtt](https://github.com/salanki/unifi-mqtt) - WLAN Association / Disassociation events from UniFi Controller to MQTT publisher.
- [bramstroker/UnifiMqttPublisher](https://github.com/bramstroker/UnifiMqttPublisher) - Publishes Unifi controller and AP statistics to a MQTT broker.
- [dcramer/unifi-mqtt](https://github.com/dcramer/unifi-mqtt) - UniFi to MQTT bridge.
- [jollyjinx/unifi2mqtt](https://github.com/jollyjinx/unifi2mqtt) - Publish UniFi device and client information to MQTT.

## UniFi Protect

- [keshavdv/unifi-cam-proxy](https://github.com/keshavdv/unifi-cam-proxy) - Enable non-Ubiquiti cameras to work with Unifi NVR.
- [ep1cman/unifi-protect-backup](https://github.com/ep1cman/unifi-protect-backup) - Python tool to backup unifi event clips in realtime.
- [petergeneric/unifi-protect-remux](https://github.com/petergeneric/unifi-protect-remux) - Converts Ubiquiti's proprietary .ubv files into standard MP4 files.
- [yuppity/unifi-video-api](https://github.com/yuppity/unifi-video-api) - Python API for UniFi Video.
- [kk7ds/luvs](https://github.com/kk7ds/luvs) - Lightweight Unifi Video Server.
- [hjdhjd/unifi-access](https://github.com/hjdhjd/unifi-access) - A nearly complete implementation of the UniFi Access API.
- [selfhostedhome/unifi-video-gif-mqtt](https://github.com/selfhostedhome/unifi-video-gif-mqtt) - Watch your UniFi Video directory for new videos, convert to gif and notify over mqtt.
- [bluewalk/unifi-udm-protect-mqtt](https://github.com/bluewalk/unifi-udm-protect-mqtt) - A Docker container to parse UniFi protect eventlog and publish motion events to MQTT.
- [bdraco/pyunifiprotect](https://github.com/bdraco/pyunifiprotect) - Python Wrapper for the Unifi Protect API.

## UniFi Access

- [jeffreykog/unifi-inform-protocol](https://github.com/jeffreykog/unifi-inform-protocol) - Information about the reverse engineered inform protocol used in Ubiquiti's UniFi access points.
- [keithah/unifi-access-airbnb](https://github.com/keithah/unifi-access-airbnb) - Integrates UniFi Access with Airbnb reservations using ICS file or Hostex API.
- [matejgordon/unipyAccess](https://github.com/matejgordon/unipyAccess) - Python connector for UniFi Access.
- [kleo/unipi](https://github.com/kleo/unipi) - WiFi voucher vending machine leveraging UniFi controller and UniFi access points.
- [phamels/unifi_access_unlocker](https://github.com/phamels/unifi_access_unlocker) - Unlock Unifi Access doors using their own API.
- [uxico-dev/unifi-access-api](https://github.com/uxico-dev/unifi-access-api) - A PHP API client for the Ubiquiti Unifi Access API.

## UniFi Talk

- [Gamer08YT/UniFi-Softphone](https://github.com/Gamer08YT/UniFi-Softphone) - Unofficial UniFi Talk Softphone.
- [Gamer08YT/UniFi-Talk-Repo](https://github.com/Gamer08YT/UniFi-Talk-Repo) - Unofficial collection of SIP templates for UniFi Talk.

## Network Automation & IaC

- [paultyng/terraform-provider-unifi](https://github.com/paultyng/terraform-provider-unifi) - Terraform provider for Unifi.
- [pulumiverse/pulumi-unifi](https://github.com/pulumiverse/pulumi-unifi) - Pulumi provider for Unifi network gear.
- [ppouliot/ansible-role-ubnt_platform_mgmt](https://github.com/ppouliot/ansible-role-ubnt_platform_mgmt) - Ansible role for managing UBNT EdgeMAX and UniFI network devices.
- [erwanclx/UnifiAnsibleModule](https://github.com/erwanclx/UnifiAnsibleModule) - Unofficial Unifi Ansible Module.
- [ferventgeek/unifi-firewall-group-updater](https://github.com/ferventgeek/unifi-firewall-group-updater) - Automate Firewall IP Group management on Unifi Controllers.

## Security Tools

- [wolffcatskyy/crowdsec-unifi-bouncer](https://github.com/wolffcatskyy/crowdsec-unifi-bouncer) - Install and persist the official CrowdSec firewall bouncer on UniFi OS devices.
- [wolffcatskyy/crowdsec-unifi-parser](https://github.com/wolffcatskyy/crowdsec-unifi-parser) - CrowdSec parsers and iptables LOG rules for UniFi Dream Machines.
- [LordOfPolls/Unifi-Rampart](https://github.com/LordOfPolls/Unifi-Rampart) - Automated threat intelligence for UniFi firewalls - syncs IP lists from Spamhaus, Firehol, abuse.ch.
- [trek-e/unifi-security-report](https://github.com/trek-e/unifi-security-report) - A containerized service that monitors UniFi network logs and delivers plain-English reports.
- [shrisha/SilenceTheLAN](https://github.com/shrisha/SilenceTheLAN) - iOS app to manage UniFi Firewall policies created for kids' downtime.
- [coolcat1575/netwatcher](https://github.com/coolcat1575/netwatcher) - Monitor your network for unknown MAC addresses using data from UniFi.

## DNS & DDNS

- [willswire/unifi-ddns](https://github.com/willswire/unifi-ddns) - Cloudflare DDNS (Dynamic DNS) support for UniFi OS.
- [kashalls/external-dns-unifi-webhook](https://github.com/kashalls/external-dns-unifi-webhook) - External-DNS Webhook to manage UniFi DNS Records.
- [evaneaston/udm-host-records](https://github.com/evaneaston/udm-host-records) - Scripts to list, add, update, and remove host records in the Ubiquiti UniFI Dream Machine DNS forwarder.
- [wicol/unifi-dns](https://github.com/wicol/unifi-dns) - A dnsmasq being populated by aliases/name overrides made in a UniFi controller.
- [ymichel/dnsmasqAdBlockUDM](https://github.com/ymichel/dnsmasqAdBlockUDM) - Dnsmasq based Ad blocking for Unifi equipment (UDM-SE and UDM-PRO).
- [missuo/unifi-cloudflare-ddns](https://github.com/missuo/unifi-cloudflare-ddns) - Cloudflare DDNS for UniFi OS.
- [jsumners/udm-dns](https://github.com/jsumners/udm-dns) - A Dnsmasq Docker container that polls a UDM-PRO for a list clients to serve as hostnames.
- [pridkett/unifi-dns-scripts](https://github.com/pridkett/unifi-dns-scripts) - Give yourself greater control over outbound DNS on your network.

## VPN & WireGuard

- [WireGuard/wireguard-vyatta-ubnt](https://github.com/WireGuard/wireguard-vyatta-ubnt) - WireGuard for Ubiquiti Devices.
- [SierraSoftworks/tailscale-udm](https://github.com/SierraSoftworks/tailscale-udm) - Run Tailscale on your Unifi Dream Machine.
- [jamesog/tailscale-edgeos](https://github.com/jamesog/tailscale-edgeos) - Running Tailscale on Ubiquiti EdgeOS.
- [tusc/wireguard-kmod](https://github.com/tusc/wireguard-kmod) - WireGuard for UDM series routers.
- [mafredri/vyatta-wireguard-installer](https://github.com/mafredri/vyatta-wireguard-installer) - Install, upgrade or remove WireGuard on Ubiquiti hardware.
- [vchrizz/ER-wizard-WireGuard](https://github.com/vchrizz/ER-wizard-WireGuard) - WireGuard Wizard for Ubiquiti EdgeMAX Devices.
- [evie-lau/Unifi-gateway-wpa-supplicant](https://github.com/evie-lau/Unifi-gateway-wpa-supplicant) - Setup wpa_supplicant on Unifi Gateways to bypass ATT modem.
- [gridironsolutions/unifios-tailscale](https://github.com/gridironsolutions/unifios-tailscale) - Run Tailscale natively on Unifi UDM-Pro Dream Machine.

## Backup Tools

- [zhangyoufu/unifi-backup-decrypt](https://github.com/zhangyoufu/unifi-backup-decrypt) - Decrypt UniFi Network Application backup (.unf to .zip).
- [psitem/edgerouter-backup](https://github.com/psitem/edgerouter-backup) - EdgeRouter to Git repo backup scripts.

## CLI Tools

- [57/unifidash](https://github.com/57/unifidash) - UniFi CLI leveraging private gateway APIs for network telemetry, DPI, and topology.
- [xezpeleta/unifi-cli](https://github.com/xezpeleta/unifi-cli) - Unifi CLI tool.

## Guest Portal & Vouchers

- [glenndehaan/unifi-voucher-site](https://github.com/glenndehaan/unifi-voucher-site) - UniFi Voucher Site is a web-based platform for generating and managing UniFi network guest vouchers.
- [PaintSplasher/unifi-voucher-service](https://github.com/PaintSplasher/unifi-voucher-service) - Simple one-click voucher printing for guests without UniFi Controller access.
- [DJM0/unifi-voucher-generator](https://github.com/DJM0/unifi-voucher-generator) - Generates UniFi Hotspot vouchers using the UniFi controller API ready for printing.
- [etiennecollin/unifi-voucher-manager](https://github.com/etiennecollin/unifi-voucher-manager) - A touch-friendly and secure interface for streamlined creation and management of guest Wi-Fi vouchers.
- [Carlgo11/guest-portal](https://github.com/Carlgo11/guest-portal) - External UniFi guest portal.
- [seanmavley/unifi-guest-bundle-check](https://github.com/seanmavley/unifi-guest-bundle-check) - Let Unifi Guests check voucher data bundle left.
- [emanuelepaiano/jespresso-lite](https://github.com/emanuelepaiano/jespresso-lite) - Espresso Ubiquiti Unifi Guest Portal written in Java / Typescript.
- [seanmavley/unifi-voucher-payment-server](https://github.com/seanmavley/unifi-voucher-payment-server) - Unifi Voucher Payment Server.
- [batesta/whoshere](https://github.com/batesta/whoshere) - Who's Here? - An automatic "In/Out" board for UniFi networks.

## Dream Machine Utilities

- [kchristensen/udm-le](https://github.com/kchristensen/udm-le) - Let's Encrypt support for Ubiquiti UniFi OS.
- [fabianishere/udm-iptv](https://github.com/fabianishere/udm-iptv) - Helper tool for configuring routed IPTV on the UniFi Dream Machine (Pro).
- [fabianishere/udm-kernel-tools](https://github.com/fabianishere/udm-kernel-tools) - Tools for bootstrapping custom kernels on the UniFi Dream Machine.
- [iceteaSA/ucg-max-fan-control](https://github.com/iceteaSA/ucg-max-fan-control) - UXG-Max/Fibre Dynamic Fan Control.
- [alxwolf/ubios-cert](https://github.com/alxwolf/ubios-cert) - Manage SSL / TLS certificates with acme.sh for Ubiquiti UbiOS firmwares.
- [fabianishere/udm-kernel](https://github.com/fabianishere/udm-kernel) - Custom Linux kernels for the UniFi Dream Machine.
- [renedis/ubnt-auto-fan-speed](https://github.com/renedis/ubnt-auto-fan-speed) - Automatic fan speed setting on UDM-PRO 1.8.5+ firmware.
- [TobyAnscombe/udm-setup](https://github.com/TobyAnscombe/udm-setup) - Simple readme for setting up IoT and VLANS on the Unifi Dream Machine.
- [davidjenni/udm-pro-network](https://github.com/davidjenni/udm-pro-network) - Unifi UDM-Pro prosumer network configuration.
- [cdchris12/UDM-DNS-Fix](https://github.com/cdchris12/UDM-DNS-Fix) - A simple script to provide basic DHCP hostname resolution in the latest UniFi Dream Machine Pro firmware.
- [blackjid/inadyn-cloudflare](https://github.com/blackjid/inadyn-cloudflare) - Cloudflare Dynamic DNS backend for Inadyn - for use with Unifi Dream Machine / Pro.
- [scyto/multicast-relay](https://github.com/scyto/multicast-relay) - Multicast-relay Docker for UniFi Dream Machines.
- [IngmarStein/unifi-sonos-doc](https://github.com/IngmarStein/unifi-sonos-doc) - How to configure your UniFi network for Sonos.
- [esmith443/Verizon-ONT-Bypass](https://github.com/esmith443/Verizon-ONT-Bypass) - Unifi UDM Pro Iszo XPON UNO Verizon FiOS.
- [ddominet/UDMPRO-samba](https://github.com/ddominet/UDMPRO-samba) - UDM-PRO drive bay as a network drive.
- [dlk3/udm-hacks](https://github.com/dlk3/udm-hacks) - Hacks for Unifi Dream Machine (UDM) Pro.
- [kalenarndt/udmp-jumbo-frames](https://github.com/kalenarndt/udmp-jumbo-frames) - Shell script to configure and monitor jumbo frame configuration on the UDM Pro.
- [xpherism/udm-proxy](https://github.com/xpherism/udm-proxy) - Caddy proxy for Ubiquiti UDM Pro.
- [whi-tw/macvlan-unifios](https://github.com/whi-tw/macvlan-unifios) - Macvlan kernel module for UniFi OS devices.
- [johnstonjs/unifios-utils](https://github.com/johnstonjs/unifios-utils) - UniFi OS Utilities.

## EdgeRouter / EdgeOS

- [jaysoffian/eap_proxy](https://github.com/jaysoffian/eap_proxy) - Proxy EAP packets between interfaces on Linux devices such as the Ubiquiti Networks EdgeRouter and UniFi Security Gateway.
- [j-c-m/ubnt-letsencrypt](https://github.com/j-c-m/ubnt-letsencrypt) - Let's Encrypt setup instructions for Ubiquiti EdgeRouter.
- [britannic/blacklist](https://github.com/britannic/blacklist) - Blacklist and Adware Blocking for the Ubiquiti EdgeMax Router.
- [WaterByWind/edgeos-bl-mgmt](https://github.com/WaterByWind/edgeos-bl-mgmt) - Automated updating of EdgeOS firewall network-group to be used as source address blacklist.
- [stevejenkins/UBNT-EdgeRouter-Example-Configs](https://github.com/stevejenkins/UBNT-EdgeRouter-Example-Configs) - Example config.boot files for UBNT EdgeRouters with Google, Comcast, and Charter.
- [hungnguyenm/edgemax-acme](https://github.com/hungnguyenm/edgemax-acme) - Let's Encrypt setup instructions for Ubiquiti EdgeRouter using DNS-01.
- [photinus/ubnt-letsencrypt](https://github.com/photinus/ubnt-letsencrypt) - Let's Encrypt setup instructions for Ubiquiti Edgerouter Lite.
- [whiskerz007/ubnt_get_wireguard](https://github.com/whiskerz007/ubnt_get_wireguard) - Get WireGuard on Ubiquiti devices.
- [brianredbeard/edgeos_setup](https://github.com/brianredbeard/edgeos_setup) - Sensible defaults for EdgeOS based routers.
- [Genghis1227/guide_eap_proxy](https://github.com/Genghis1227/guide_eap_proxy) - Instructions for AT&T bypass using EdgeRouter Lite.
- [Matthew1471/EdgeOS-API](https://github.com/Matthew1471/EdgeOS-API) - An API wrapper for Ubiquiti EdgeOS operating system.
- [darkgrue/Ubiquiti-DNSCrypt-Proxy-2-Configuration-Scripts](https://github.com/darkgrue/Ubiquiti-DNSCrypt-Proxy-2-Configuration-Scripts) - Support scripts for DNSCrypt-Proxy 2, dnsmasq, and DNSSEC on Edgerouter.
- [darkxst/erx-migration](https://github.com/darkxst/erx-migration) - Openwrt: Edgerouter X migration scripts for installing or upgrading to Openwrt.
- [neilalexander/vyatta-cjdns](https://github.com/neilalexander/vyatta-cjdns) - A cjdns package for Ubiquiti EdgeOS and VyOS.
- [amarcu5/EdgeOS-Blacklist](https://github.com/amarcu5/EdgeOS-Blacklist) - Automatically updates IP blacklist for EdgeOS (supports IPv4 and IPv6).
- [sowbug/mkeosimg](https://github.com/sowbug/mkeosimg) - Make a Ubiquiti EdgeOS image from a system tarball.

## MCP Servers

- [sirkirby/unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp) - MCP server implementation for the UniFi network application.
- [enuno/unifi-mcp-server](https://github.com/enuno/unifi-mcp-server) - An MCP server that leverages official UniFi API.
- [bjeans/homelab-mcp](https://github.com/bjeans/homelab-mcp) - MCP servers for managing homelab infrastructure including UniFi networks.

## Guides & Documentation

- [mzac/unifi-pfsense-tailscale](https://github.com/mzac/unifi-pfsense-tailscale) - Documentation on how to integrate Unifi with pfSense and Tailscale.
- [beezly/unifi-apis](https://github.com/beezly/unifi-apis) - UniFi Network and Protect API OpenAPI specifications.
- [ubiquiti-community/unifi-api](https://github.com/ubiquiti-community/unifi-api) - OpenAPI Definition for Unifi Controller API.
- [MinisculeGirraffe/Tailscale-UDMPro](https://github.com/MinisculeGirraffe/Tailscale-UDMPro) - Guide to running Tailscale on a UDM(Pro).

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.
