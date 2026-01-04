================================================
## PROJECT PREDATOR – AJANLAR ARASI VERİ AĞI HARİTASI
## (SINGLE SOURCE OF TRUTH – DATA FLOW MAP)
================================================

Amaç:
Bu doküman, PROJECT PREDATOR içindeki TÜM ajanların
birbirleriyle hangi verileri, hangi yönde,
hangi yetkiyle paylaştığını kesin ve kapalı biçimde tanımlar.

Bu harita:
- Yetki ihlallerini önler
- Gizli feedback loop’ları engeller
- Otonomiyi kontrollü kılar
- Denetlenebilirliği garanti eder

================================================
## 1. YÜKSEK SEVİYE ANA VERİ AKIŞI (OMURGA)
================================================

RAW MARKET DATA
      ↓
Market Scanner Agent
      ↓
Strategist MCP
      ↓
CRO / Risk Agent
      ↓
Portfolio Manager Agent
      ↓
Execution / Trader Agent
      ↓
KPI / Performance Analyst
      ↓
(HUMAN OBSERVATION)

Bu omurga DIŞINDA hiçbir ajan,
doğrudan trade kararına bağlanamaz.

================================================
## 2. AJAN BAZLI DETAYLI VERİ AKIŞI
================================================

------------------------------------------------
## 2.1 MARKET SCANNER AGENT
------------------------------------------------

ALDIĞI VERİLER:
- OHLCV (ham piyasa verisi)
- Likidite metrikleri
- Volatilite ölçümleri
- Piyasa aktif/pasif durumu

ÜRETTİĞİ VERİLER:
- CandidateCoinList
- CoinMetadata:
  - Likidite skoru
  - Volatilite skoru
  - Davranış etiketi (trend / range / spike)

GÖNDERDİĞİ:
- ➜ Strategist MCP

ASLA GÖNDEREMEZ:
- Sinyal
- Emir
- Risk yorumu
- Strateji kararı

------------------------------------------------
## 2.2 STRATEGIST MCP
------------------------------------------------

ALDIĞI VERİLER:
- CandidateCoinList (Scanner)
- Historical Market Data (Data Agent)
- Oracle Context Flags (OPSİYONEL)

ÜRETTİĞİ VERİLER:
- StrategyProposal
- BacktestReport
- StrategyScore
- RegimeCompatibility

GÖNDERDİĞİ:
- ➜ CRO / Risk Agent (onay için)
- ➜ KPI Analyst (okuma amaçlı)

ASLA GÖNDEREMEZ:
- Trade emri
- Sermaye tahsisi
- Risk kuralı

------------------------------------------------
## 2.3 ORACLE AGENT
------------------------------------------------

ALDIĞI VERİLER:
- Haber akışları
- Sosyal medya sentiment (agregasyon)
- Event / takvim verileri

ÜRETTİĞİ VERİLER:
- ContextFlag (RISK_ON / RISK_OFF / NEUTRAL)
- ExternalAnomalyAlert

GÖNDERDİĞİ:
- ➜ Strategist MCP (opsiyonel, bağlayıcı değil)
- ➜ Compliance Agent (bilgi amaçlı)

ASLA GÖNDEREMEZ:
- Sinyal
- Tavsiye
- Risk kararı

------------------------------------------------
## 2.4 CRO / RISK AGENT
------------------------------------------------

ALDIĞI VERİLER:
- StrategyProposal (Strategist)
- PnL & Drawdown (KPI)
- Sistem durumu
- Exposure özetleri

ÜRETTİĞİ VERİLER:
- APPROVE / VETO
- HALT / RESUME
- RiskAlert

GÖNDERDİĞİ:
- ➜ Portfolio Manager
- ➜ Execution Agent (HALT sinyali)
- ➜ Compliance Agent (kayıt)

ASLA GÖNDEREMEZ:
- Strateji fikri
- Optimizasyon
- Sermaye dağılımı

------------------------------------------------
## 2.5 PORTFOLIO MANAGER AGENT
------------------------------------------------

ALDIĞI VERİLER:
- CRO onaylı stratejiler
- Portföy durum özetleri

ÜRETTİĞİ VERİLER:
- AllocationPlan
- StrategyActivation / Deactivation

GÖNDERDİĞİ:
- ➜ Execution / Trader Agent
- ➜ KPI Analyst

ASLA GÖNDEREMEZ:
- Risk kuralı
- Strateji üretimi
- Emir detayı yorumu

------------------------------------------------
## 2.6 EXECUTION / TRADER AGENT
------------------------------------------------

ALDIĞI VERİLER:
- AllocationPlan (PM)
- HALT / PAUSE sinyalleri (CRO / Sentinel)

ÜRETTİĞİ VERİLER:
- OrderResult
- FillReport
- ExecutionError
- Slippage / Latency Metrics

GÖNDERDİĞİ:
- ➜ KPI Analyst
- ➜ Compliance Agent
- ➜ Developer MCP (hata durumunda)

ASLA GÖNDEREMEZ:
- Öğrenme geri bildirimi
- Tavsiye
- Karar

------------------------------------------------
## 2.7 KPI / PERFORMANCE ANALYST
------------------------------------------------

ALDIĞI VERİLER:
- Execution sonuçları
- Allocation snapshot’ları
- PnL zaman serileri

ÜRETTİĞİ VERİLER:
- KPI Report
- Performance Summary
- Drawdown Analysis

GÖNDERDİĞİ:
- ➜ Human
- ➜ CRO / Risk Agent
- ➜ Compliance Agent
- ➜ Strategist MCP (READ-ONLY)

ASLA GÖNDEREMEZ:
- Karar
- Tavsiye
- Promosyon talimatı

------------------------------------------------
## 2.8 COMPLIANCE AGENT
------------------------------------------------

ALDIĞI VERİLER:
- TÜM ajan logları
- TÜM karar kayıtları
- Faz durumu

ÜRETTİĞİ VERİLER:
- BLOCK / FREEZE
- PHASE CLEARANCE
- AuditReport

GÖNDERDİĞİ:
- ➜ TÜM AJANLAR (yetki bazlı)

ASLA GÖNDEREMEZ:
- Yorum
- Optimizasyon
- Tavsiye

------------------------------------------------
## 2.9 RATELIMIT & RESOURCE SENTINEL
------------------------------------------------

ALDIĞI VERİLER:
- API çağrı sayaçları
- CPU / RAM / Disk / Event Loop

ÜRETTİĞİ VERİLER:
- THROTTLE
- PAUSE
- DEGRADED MODE
- EmergencyAlert

GÖNDERDİĞİ:
- ➜ TÜM AJANLAR
- ➜ CRO (acil durum)

------------------------------------------------
## 2.10 DEVELOPER MCP
------------------------------------------------

ALDIĞI VERİLER:
- Error logs
- Sentinel uyarıları
- Crash raporları

ÜRETTİĞİ VERİLER:
- Patch
- Restart
- IncidentReport

GÖNDERDİĞİ:
- ➜ Compliance Agent
- ➜ Human

================================================
## 3. MUTLAK YASAK VERİ AKIŞLARI
================================================

- Strategist ➜ Execution  ❌
- Oracle ➜ Portfolio     ❌
- KPI ➜ Karar            ❌
- Execution ➜ Öğrenme    ❌
- Herhangi bir ajan ➜ Compliance override ❌

================================================
## 4. TEK CÜMLELİK ÖZET
================================================

PROJECT PREDATOR’da veri akışı TEK YÖNLÜDÜR:
bilgi yukarı çıkar, karar aşağı iner,
hiçbir ajan hem düşünen hem uygulayan olamaz.

================================================
# END OF AGENT DATA FLOW MAP
================================================
