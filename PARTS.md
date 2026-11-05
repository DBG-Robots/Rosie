# Rosie – picked parts

JLCPCB **Economic PCBA only**. Basic/Preferred parts are free; each unique Extended part costs $3.07 per order.
Every pick below was checked as Economic-eligible and in stock on 2026-11-03 (power parts for the 4×AA design: 2026-11-04).

**Battery:** 4×AA in a flat holder under the board (NiMH 1900–2500 mAh, about 3 h; alkaline works too), 4.0–6.4 V.
The board never charges the cells: charge them in an external AA charger.
Resistors and capacitors aren't listed: JLC matches them by value and package. R43–R58 are 1 kΩ series resistors protecting every encoder, servo, UART and GPIO signal, so the pins on J12 can only source or sink about 1–2 mA. R59–R63 are the debug LED resistors (see below). Pick C47 (10 µF on VBUS) rated at least 16 V, because plugging in a USB cable can briefly overshoot 5 V.

## Assembled by JLC

| Function | Part | LCSC | Symbol | Footprint |
|---|---|---|---|---|
| Motor driver ×2 | DRV8833PWPR | C50506 | `Driver_Motor:DRV8833PWP` | `Package_SO:HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm_Mask2.46x2.31mm_ThermalVias` |
| 3.3 V buck (3–17 V in, 3 A, 100 % duty) | TPS62130ARGTR | C337502 | `Regulator_Switching:TPS62130A` | `Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm_ThermalVias` |
| Servo eFuse (2 A, no OV clamp, auto-retry) | TPS259571DSGR | C471038 | `jlc:TPS259571DSG` | `Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm` |
| Schottky ×3 (D6, D7: logic supply OR, battery / USB; D8: servo output clamp) | SS34 | C8678 (Basic) | `Diode:SS34` | `Diode_SMD:D_SMA` |
| Resettable fuse (3 A hold / 5 A trip, 8 V) | ASMD1812-300 | C135366 | `Device:Polyfuse` | `Fuse:Fuse_1812_4532Metric` |
| 5 V boost (from 3.3 V) | TPS61023DRLR | C919459 | `jlc:TPS61023DRL` | `Package_TO_SOT_SMD:SOT-563` |
| Current-limited switch ×2 (ext. 5 V / ext. 3.3 V) | SY6280AAC | C55136 | `jlc:SY6280AAC` | `Package_TO_SOT_SMD:SOT-23-5` |
| 1 µH inductor ×2 (18 mΩ, 4.7 A / 5.7 A) | FNR4030S1R0MT | C167865 | `Device:L` | `Inductor_SMD:L_Changjiang_FNR4030S` |
| P-FET ×2 (battery reverse polarity, power switch) | AO3401A | C15127 (Basic) | `Transistor_FET:AO3401A` | `Package_TO_SOT_SMD:SOT-23` |
| Qwiic I2C socket (J7) | JST SM04B-SRSS-TB(LF)(SN) | C160404 | `Connector_Generic:Conn_01x04` | `Connector_JST:JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal` |
| USB ESD | USBLC6-2SC6 | C7519 | `Power_Protection:USBLC6-2SC6` | `Package_TO_SOT_SMD:SOT-23-6` |
| USB-C receptacle | HRO TYPE-C-31-M-12 | C165948 | `Connector:USB_C_Receptacle_USB2.0_16P` | `Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12` |
| RGB LED (WS2812B-compatible, 1 VDD / 2 DO / 3 GND / 4 DI) | XL-5050RGBC-2812B-HM | C48586674 | `LED:WS2812B` | `LED_SMD:LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm` |
| Buzzer (magnetic, 16 Ω) | MLT-8530 | C94599 | `Device:Buzzer` | `jlc:Buzzer_Huaneng_MLT-8530` |
| Buzzer driver NPN | MMBT3904 | C20526 (Basic) | `Transistor_BJT:MMBT3904` | `Package_TO_SOT_SMD:SOT-23` |
| Diode (buzzer flyback, RGB LED supply drop) | 1N4148WS | C2128 (Basic) | `Diode:1N4148WS` | `Diode_SMD:D_SOD-323` |
| Power LEDs, green (D2 3V3, D9 USB, D10 BAT ON) | KT-0805G | C2297 (Basic) | `Device:LED_Small` | `LED_SMD:LED_0805_2012Metric` |
| Motors-enabled LED, yellow (D12 MOT ON) | KT-0805Y | C2296 (Basic) | `Device:LED_Small` | `LED_SMD:LED_0805_2012Metric` |
| Fault LEDs, red (D11 MOT ERR, D13 SRV ERR) | KT-0603R | C2286 (Basic) | `Device:LED_Small` | `LED_SMD:LED_0603_1608Metric` |
| EN / BOOT buttons | TS-1187A-B-A-B | C318884 (Basic) | `Switch:SW_Push` | `Button_Switch_SMD:SW_Push_1P1T_XKB_TS-1187A` |

## Hand-soldered (order from LCSC, not placed by JLC)

| Function | Part | LCSC | Symbol | Footprint |
|---|---|---|---|---|
| MCU module | ESP32-S3-WROOM-1-N8R2 | C2913204 | `RF_Module:ESP32-S3-WROOM-1` | `jlc:ESP32-S3-WROOM-1_HandSolder` (longer pads, no paste, solder hole in the ground pad) |
| Power slide switch (right-angle) | SK12D07VG4 | C393937 | `Switch:SW_SPDT` | `Button_Switch_THT:SW_Slide_SPDT_Angled_CK_OS102011MA1Q` |
| Battery connector (keyed, 3 A) | XH-2A (JST XH 2-pin) | C2908600 | `Connector_Generic:Conn_01x02` | `Connector_JST:JST_XH_B2B-XH-A_1x02_P2.50mm_Vertical` |
| Battery holder | flat 4×AA holder with leads + JST-XH 2-pin pigtail (pin 1 = +) | – (any shop) | – | – |
| Motor + encoder connector ×2–4 (JST ZH 1.5 mm; 1 M1, 2 GND, 3 C1, 4 C2, 5 VCC, 6 M2) | JST B6B-ZR(LF)(SN) | C157984 | `Connector_Generic:Conn_01x06` | `jlc:JST_ZH_B6B-ZR_1x06_P1.50mm_Vertical` |
| Pin headers: servos, UART, GPIO, I2C (J8) | 1×40 male 2.54 mm (cut to length) | C42431788 | `Connector_Generic:Conn_01x0x` | `Connector_PinHeader_2.54mm:…` |

## Debug LEDs and test pads (Debug sheet)

None of this is needed for the robot to run. Green means power, yellow means motors enabled, red means a fault.

| LED | Silk | Lights when | Wiring |
|---|---|---|---|
| D2, green | 3V3 | +3V3 rail is up | +3V3 → R26 1 k → GND |
| D9, green | USB | USB power is present | VBUS → R59 4.7 k → GND |
| D10, green | BAT ON | switch on and battery connected | VSYS → R60 4.7 k → GND |
| D12, yellow | MOT ON | firmware enables the motor drivers | MOT_EN → R62 470 Ω → GND |
| D11, red | MOT ERR | a DRV8833 reports overcurrent, overheating or undervoltage | +3V3 → R61 1 k → MOT_FAULT |
| D13, red | SRV ERR | the servo eFuse overheats and shuts down (it doesn't light for current limiting alone) | +3V3 → R63 1 k → SERVO_FLT (TPS259571 pin 6) |

Test pads are 1.5 mm bare pads on the top side, with no part fitted and not in the BOM or position file.

| Silk | Net | Silk | Net |
|---|---|---|---|
| BAT | +BATT | 5VX | +5V_EXT |
| VSYS | VSYS | VSRV | VSERVO |
| VBUS | VBUS | GND (3 pads) | GND |
| VLOG | VLOGIC | EN | EN |
| 3V3 | +3V3 | BOOT | BOOT |
| 5V | +5V | M_EN / M_FLT | MOT_EN / MOT_FAULT |
| 3V3X | +3V3_EXT | VBAT | VBAT_SENSE |

## Motors (not on the board)

The motor connectors match the CHIHAI CHF-GM12-N20 hall-encoder motor, 6 V, with its 6-pin ZH 1.5 mm cable. Other N20 motors use other pin orders, and a wrong order can swap encoder VCC and GND.
Before first power, plug the motor into the unpowered board and check with a multimeter that the GND pad on the encoder connects to board GND.

## PCB

4 layers, 80×72 mm: top = parts and power routing, In1 = solid GND, In2 = +3V3 plane with thin +3V3_EXT, +5V and VBUS traces, bottom = free for signals.

## Project library (`libs/`)

- `jlc.kicad_sym`: TPS259571DSG, TPS61023DRL, SY6280AAC (drawn from the datasheets; KiCad's stock library doesn't have them), plus power symbols VSYS, VSERVO, +3V3_EXT, +5V_EXT
- `jlc.pretty`: ESP32-S3-WROOM-1_HandSolder, Buzzer_Huaneng_MLT-8530, JST_ZH_B6B-ZR_1x06_P1.50mm_Vertical (drawn from the JST datasheet; KiCad's stock library has no ZH), SOT-563_TI_DRL (TI's land pattern), and copies of the stock HTSSOP-16 and VQFN-16 footprints with 0.3 mm thermal vias (`_D0.3`)
- `jlc.3dshapes`: ESP32-S3-WROOM-1.step, plus simplified models of the buzzer, ZH connector, USB-C receptacle, tact switch and fuse. They are drawn from the datasheet outlines by `libs/3d-generator/make_models.py` (run with FreeCAD), so sizes, heights and pin positions are right but small details are missing.
- The stock KiCad footprints for the USB-C connector, the tact switches and the fuse point to model files that this KiCad install doesn't have, so the board uses the generated models for them. The two DRV8833s and the TPS62130 use the stock STEP models of the same packages.

## Resistors and capacitors (JLC part numbers)

Looked up on 2026-11-05: all in stock and Economic-eligible. **Basic** parts cost nothing extra; **Extended** parts cost $3.07 per unique part per order.

| Value | Package | Parts | LCSC | Type |
|---|---|---|---|---|
| 100 nF | 0402 | C2 C16 C23 C36 C40 C44 | C1525 (16 V) | Basic |
| 10 nF | 0402 | C28 C38 C42 | C15195 (50 V) | Basic |
| 1 µF | 0402 | C3 | C52923 (25 V) | Basic |
| 2.2 µF | 0402 | C37 C41 | C12530 (6.3 V, fine for the DRV8833 VINT pin) | Basic |
| 4.7 nF | 0402 | C24 C48 | C1538 (50 V) | Basic |
| 10 µF | 0603 | C1 | C19702 (10 V) | Basic |
| 10 µF | 0805 | C22 C27 C31–C35 C39 C45 C46 C47 | C15850 (25 V, also covers C47's 16 V rule) | Basic |
| 22 µF | 0805 | C17 C18 C21 C25 C26 C29 C30 C43 | C45783 (25 V) | Basic |
| 1 kΩ | 0402 | 21 parts (series, LED and pull resistors) | C11702 | Basic |
| 10 kΩ | 0402 | R1 R2 R30 R33 R39 | C25744 | Basic |
| 100 kΩ | 0402 | R14 R17 R41 | C25741 | Basic |
| 2 kΩ | 0402 | R28 | C4109 | Basic |
| 15 kΩ | 0402 | R25 R27 | C25756 | Basic |
| 47 kΩ | 0402 | R24 | C25792 | Basic |
| 4.7 kΩ | 0402 | R36 R37 R59 R60 | C25900 | Basic |
| 470 Ω | 0402 | R62 | C25117 | Basic |
| 5.1 kΩ | 0402 | R9 R10 | C25905 | Basic |
| 12 kΩ | 0402 | R29 | C25752 | Basic |
| 200 kΩ | 0402 | R13 R40 | C25764 | Basic |
| 0.2 Ω 1 % | 1206 | R31 R32 R34 R35 | C160920 | **Extended** |

Extended parts per order: 12 ICs and connectors (DRV8833, TPS62130A, TPS259571, TPS61023, SY6280, FNR4030S, USBLC6, USB-C, SM04B-SRSS, XL-5050 RGB, MLT-8530, ASMD1812) plus the 0.2 Ω current-sense resistors above, so 13 × $3.07 ≈ $40 per order. Six Extended passives were swapped for Basic values on 2026-11-05 (saving about $18 per order): the 3.3 V, 5 V and servo-eFuse dividers were recalculated (see below), R30 went from 8.2 k to 10 k, and C24 from 3.3 nF to 4.7 nF. Nothing here is tested on hardware. R13 and R14 were renamed from "200k/1%" and "100k/1%" to plain "200k" and "100k" on 2026-11-05, because JLC matched the odd value text to two Extended parts.

| Change | New value | Result |
|---|---|---|
| 3.3 V divider R24/R25 | 47 k / 15 k | 0.8 V × (1 + 47/15) = 3.31 V (was 3.29 V) |
| 5 V divider R27/R28, feed-forward C28 | 15 k / 2 k, 10 nF | 0.595 V × (1 + 15/2) = 5.06 V (was 4.95 V); zero at 1/(2π × 15 k × 10 nF) = 1.06 kHz as the TPS61023 datasheet recommends. The divider now draws about 0.3 mA from the 5 V rail |
| Servo eFuse UVLO R40/R41 | 200 k / 100 k | on above 3.6 V, off below 3.3 V (was 3.75 / 3.44 V) |
| +5V_EXT limit R30 | 10 k | 6800 / 10 k = 0.68 A (was 0.83 A) |
| 3.3 V soft start C24 | 4.7 nF | 2.35 ms ramp (was 1.65 ms) |
The ASMD1812-300 holds 3.0 A at 25 °C but only 2.3 A at 50 °C and 1.6 A at 70 °C (datasheet derating table), so on a warm robot the fuse can trip at stall currents the cold board handles.

## Footprints checked against the manufacturers' datasheets (2026-11-05)

The footprints were compared with the LCSC datasheet drawings and with EasyEDA's footprints (downloaded by hand on 2026-11-05). All pad positions match; only the SOD-323 pads (D4, D5) are much smaller than EasyEDA's.
- Buzzer MLT-8530: body 8.5 × 8.5 mm, 3.0 mm high, pads at the four chamfered corners. Matches. The datasheet marks two pads as dummy (not connected inside), and the footprint ties all four to the two nets, which is harmless.
- Slide switch SK12D07VG4: pin pitch 2.0 mm, mounting tabs 8.3 mm apart (the footprint has 8.2 mm), body 8.7 × 4.4 mm. Matches. Pin 2 is the common pin.
- Tact switch TS-1187A-B-A-B: 5.1 × 5.1 mm, 1.6 mm high, pads ±3.0 × ±1.875 mm. Matches.
- USB-C TYPE-C-31-M-12: shell 8.64 mm wide, shell tabs ±4.32 mm. Matches the stock footprint.
- XH-2A: 2.5 mm pitch, 3 A. Matches `JST_XH_B2B-XH-A`.
- The datasheet for SK12D07VG4 rates the contacts at 0.5 A. That is fine because the switch only pulls the gate of Q2 low; the motor current flows through Q2.

## Power rails

| Rail | Source | Feeds |
|---|---|---|
| +BATT | 4×AA holder → F1 (resettable fuse) → Q1 (reverse-polarity P-FET) | power switch |
| VSYS | Q2 + SW3 power switch (4.0–6.4 V) | DRV8833 VM (motors), TPS259571 → VSERVO, SS34 → VLOGIC, VBAT_SENSE divider |
| VBUS | USB-C | SS34 → VLOGIC only (never motors, servos or the cells) |
| VLOGIC | higher of VSYS and VBUS, through SS34 ×2 | TPS62130A |
| +3V3 | TPS62130A buck (3.31 V) | ESP32, I2C pull-ups, buzzer, TPS61023, SY6280 → +3V3_EXT |
| +5V | TPS61023 boost from +3V3 (5.06 V) | RGB LED (via 1N4148), SY6280 → +5V_EXT |
| VSERVO | TPS259571 eFuse, 2.0 A limit (on above 3.6 V, off below 3.3 V; 4.0–6.4 V) | servo headers |
| +3V3_EXT | SY6280, 0.57 A limit | encoders, I2C headers, GPIO header |
| +5V_EXT | SY6280, 0.68 A limit | lidar UART header |

## GPIO plan (ESP32-S3-WROOM-1-N8R2)

| GPIO | Net | Notes |
|---|---|---|
| IO6 / IO7 | M1_IN1 / M1_IN2 | DRV8833 PWM inputs (MCPWM or LEDC) |
| IO16 / IO15 | M2_IN1 / M2_IN2 | DRV8833 PWM inputs |
| IO37 / IO38 | M3_IN1 / M3_IN2 | DRV8833 PWM inputs |
| IO40 / IO39 | M4_IN1 / M4_IN2 | DRV8833 PWM inputs |
| IO5 / IO4 | ENC1_A / ENC1_B | quadrature encoders (PCNT, 4 units) |
| IO17 / IO18 | ENC2_A / ENC2_B | quadrature encoder |
| IO36 / IO35 | ENC3_A / ENC3_B | quadrature encoder |
| IO41 / IO42 | ENC4_A / ENC4_B | quadrature encoder |
| IO10 | MOT_EN | DRV8833 nSLEEP (internal pull-down: motors off during boot) |
| IO21 | MOT_FAULT | open drain, 10k pull-up, both drivers wired-OR |
| IO8 / IO9 | I2C_SDA / I2C_SCL | Arduino default pins, 4.7k pull-ups |
| IO11 / IO12 | SERVO1 / SERVO2 | LEDC 50 Hz PWM |
| IO43 / IO44 | UART_TX / UART_RX | UART0, lidar header |
| IO47 | BUZZER | 2.7 kHz square wave via MMBT3904 |
| IO48 | RGB_LED | WS2812B data |
| IO1, IO2, IO13, IO14 | P1, P2, P3, P4 | expansion header J12, labelled P1–P4 on the board (P1 and P2 are ADC1-capable) |
| IO3 | VBAT_SENSE | battery divider 1:3 (6.4 V → 2.13 V), ADC1_CH2; firmware: warn at 4.4 V, motors off at 4.0 V; reads 0 V when SW3 is off; ramp motors up instead of starting at full power, to avoid brownouts |
| IO0 / IO19 / IO20 | BOOT / USB_DN / USB_DP | |
| IO45, IO46 | – | strapping pins, left unconnected |
