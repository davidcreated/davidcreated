<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=700&size=38&duration=3000&pause=800&color=00D9FF&center=true&vCenter=true&width=1000&lines=Folorunsho-Roberts+David;Senior+Software+Engineer;Go+%7C+Distributed+Systems+%7C+Mobile+Architect;Building+Infrastructure+That+Scales+To+Millions" alt="Typing SVG" />
  </a>
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:00D9FF,100:7928CA&height=260&section=header&text=David%20Paul%20Folorunsho-Roberts&fontSize=48&animation=fadeIn&fontColor=ffffff&desc=Go%20Engineer%20%E2%80%A2%20Distributed%20Systems%20%E2%80%A2%20Mobile%20Architect&descAlign=50&descAlignY=72&descSize=18" width="100%"/>
</div>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=davidcreated&style=for-the-badge&color=00D9FF&labelColor=0D1117" alt="Profile Views">
  <img src="https://img.shields.io/badge/Go-Primary%20Language-00ADD8?style=for-the-badge&logo=go&logoColor=white&labelColor=0D1117" alt="Go">
  <img src="https://img.shields.io/badge/Apps%20Deployed-40%2B-success?style=for-the-badge&labelColor=0D1117" alt="Apps">
  <img src="https://img.shields.io/badge/Experience-6%2B%20Years-orange?style=for-the-badge&labelColor=0D1117" alt="Experience">
  <img src="https://img.shields.io/badge/Systems-Distributed-7928CA?style=for-the-badge&labelColor=0D1117" alt="Distributed">
</p>

<p align="center">
  <a href="https://twitter.com/davidcreated0" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white&labelColor=0D1117">
  </a>
  <a href="https://www.linkedin.com/in/david-paul-folorunsho-roberts-198650214" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0D1117">
  </a>
  <a href="mailto:timifroberts@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117">
  </a>
  <a href="https://github.com/davidcreated">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white&labelColor=0D1117">
  </a>
</p>

---

## `whoami`

```go
package main

import "fmt"

type Engineer struct {
	Name         string
	Role         string
	PrimaryLang  string
	MobileStack  []string
	Domains      []string
	Philosophy   string
}

func main() {
	me := Engineer{
		Name:        "David Paul Folorunsho-Roberts",
		Role:        "Senior Software Engineer",
		PrimaryLang: "Go",
		MobileStack: []string{"Swift", "Kotlin", "Java", "Dart/Flutter"},
		Domains: []string{
			"Distributed Systems",
			"Microservices Architecture",
			"High-Throughput APIs",
			"Native Mobile Development",
			"Cross-Platform Mobile",
			"AI Systems Integration",
		},
		Philosophy: "Design for failure. Optimize for humans. Ship for impact.",
	}

	fmt.Printf("Building systems at scale with %s\n", me.PrimaryLang)
	fmt.Printf("Crafting mobile experiences across %d platforms\n", len(me.MobileStack))
}
```

---

## ⚙️ **The Engineering Doctrine**

<img align="right" alt="Coding" width="380" src="https://raw.githubusercontent.com/devSouvik/devSouvik/master/gif3.gif">

I don't write features — **I engineer systems that outlive their deadlines.**

As a **Senior Go Engineer & Mobile Architect**, I operate at the intersection of:

- Designing **fault-tolerant distributed backends** in Go with gRPC, Kafka, and Redis
- Crafting **idiomatic Go** microservices with clean interfaces and zero dependencies noise
- Building **native mobile experiences** across iOS (Swift), Android (Kotlin/Java), and cross-platform (Dart/Flutter)
- Integrating **AI/ML pipelines** into production workflows
- Shipping **government-grade and fintech-grade** systems to millions of users

<br clear="right"/>

### 📐 **Core Competency Radar**

```
⚙️  Go & Distributed Systems     ████████████████████  100%
📱  Mobile (Swift/Kotlin/Dart)   ████████████████████  100%
🔥  Microservices / gRPC / REST  ██████████████████░░   90%
🧠  AI/ML Integration            ████████████████░░░░   80%
☁️  Cloud & Infrastructure       ██████████████████░░   90%
🔐  Security & AuthN/AuthZ       ██████████████████░░   90%
📊  Observability & SRE          ████████████████░░░░   80%
```

---

## ⚡ **Go-Powered Systems I've Built**

> Production-grade distributed systems written in Go — designed for correctness, concurrency, and scale.

---

### 🏗️ NEXUS-OMS · Order Management System

<table width="100%">
<tr>
<td width="60%" valign="top">

**A fully distributed Order Management System built on Go microservices.**

Each service is independently deployable, communicates over gRPC, and is backed by domain-isolated PostgreSQL stores. Kafka drives the event backbone — from order creation through kitchen acknowledgment, stock reservation, and payment finalization.

**Architecture:**
- `gateway/` — HTTP API Gateway, request routing + auth middleware
- `order/` — Order lifecycle state machine
- `kitchen/` — Kitchen queue consumer, fulfillment coordination
- `payments/` — Payment processor with idempotent charge handling
- `stock/` — Inventory reservation + rollback on failure
- `common/` — Shared proto contracts, error types, middleware

**Engineering Highlights:**
- Saga pattern for distributed transaction consistency
- Outbox pattern to guarantee event delivery
- Structured logging with `slog`, tracing with OpenTelemetry
- Graceful shutdown on all services via `context.WithCancel`
- Dockerized, orchestrated with Kubernetes

</td>
<td width="40%" valign="top">

```
┌─────────────────────────────┐
│         API Gateway         │
│    (Go + net/http + JWT)    │
└────────────┬────────────────┘
             │ gRPC
    ┌─────────┼──────────┐
    ▼         ▼          ▼
┌───────┐ ┌──────┐ ┌──────────┐
│ Order │ │Stock │ │ Payments │
│Service│ │  Svc │ │   Svc    │
└───┬───┘ └──┬───┘ └────┬─────┘
    │        │           │
    └────────┴─────┬─────┘
                   ▼
            ┌─────────────┐
            │    Kafka    │
            │ Event Bus   │
            └──────┬──────┘
                   ▼
            ┌─────────────┐
            │   Kitchen   │
            │   Service   │
            └─────────────┘
```

<p>
<img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
<img src="https://img.shields.io/badge/gRPC-4285F4?style=flat-square&logo=google&logoColor=white">
<img src="https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apache-kafka&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/K8s-326CE5?style=flat-square&logo=kubernetes&logoColor=white">
<img src="https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white">
</p>

</td>
</tr>
</table>

---

### 🔐 SENTINEL · High-Throughput Auth & API Gateway

<table width="100%">
<tr>
<td width="60%" valign="top">

**A custom reverse-proxy and authentication gateway written entirely in Go.**

Handles **50,000+ requests/sec** at peak with sub-2ms P99 latency. Stateless JWT validation, rate limiting via Redis sliding window, and dynamic route config via etcd — no restarts needed for config changes.

**Engineering Highlights:**
- Zero-allocation hot path using `sync.Pool` for request contexts
- Token bucket + sliding window hybrid rate limiter
- Circuit breaker per upstream service (Hystrix-inspired)
- mTLS between internal services
- Prometheus metrics + Grafana dashboards
- Live config reload via etcd watch without downtime

</td>
<td width="40%" valign="top">

```
Client Request
      │
      ▼
┌─────────────────┐
│   TLS Termina-  │
│   tion Layer    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Rate Limiter   │◄── Redis Cluster
│  (sliding win.) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  JWT Validator  │◄── JWKS Endpoint
│  + AuthZ Check  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Circuit Breaker │
│  Load Balancer  │
└────────┬────────┘
         │
    Upstream Services
```

<p>
<img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white">
<img src="https://img.shields.io/badge/etcd-419EDA?style=flat-square&logo=etcd&logoColor=white">
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white">
<img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white">
</p>

</td>
</tr>
</table>

---

### 📡 STREAMCORE · Real-Time Event Streaming Engine

<table width="100%">
<tr>
<td width="60%" valign="top">

**A Go-native event streaming and pub/sub platform for real-time applications.**

Built to replace third-party dependencies with a self-hosted solution. Supports fan-out to thousands of WebSocket subscribers, persistent event logs, and consumer group semantics — all without leaving the Go ecosystem.

**Engineering Highlights:**
- Custom WebSocket hub with goroutine-per-connection, bounded by `semaphore`
- Persistent event store backed by RocksDB (via CGO binding)
- Consumer group offset tracking in Redis
- Backpressure handling via buffered channels + drop policies
- Horizontal scaling with consistent hashing for partition ownership
- Built-in dead letter queue for unprocessable events

</td>
<td width="40%" valign="top">

```go
// Fan-out with backpressure
type Hub struct {
    clients   map[string]*Client
    broadcast chan Event
    mu        sync.RWMutex
    sem       *semaphore.Weighted
}

func (h *Hub) Publish(e Event) {
    h.mu.RLock()
    defer h.mu.RUnlock()
    for _, c := range h.clients {
        select {
        case c.send <- e:
        default:
            // drop: slow consumer
            h.dropMetric.Inc()
        }
    }
}
```

<p>
<img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
<img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socket.io&logoColor=white">
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white">
<img src="https://img.shields.io/badge/RocksDB-0080FF?style=flat-square&logo=databricks&logoColor=white">
</p>

</td>
</tr>
</table>

---

### 💳 PAYLANE · Fintech Payment Processing Engine

<table width="100%">
<tr>
<td width="50%" valign="top">

**Idempotent payment processing service written in Go.**

Handles multi-gateway routing (Paystack, Flutterwave, Stripe), reconciliation, and webhook delivery with at-least-once guarantees. Every charge is idempotent by design — double-tap protection baked into the domain model.

**Engineering Highlights:**
- Idempotency keys stored in Redis with TTL expiry
- Webhook retry engine with exponential backoff + jitter
- Multi-provider routing based on success-rate telemetry
- Double-entry ledger model for financial accuracy
- PCI-DSS scoped design: card data never touches application layer

</td>
<td width="50%" valign="top">

**Engineering Highlights (cont.):**
- Automated daily reconciliation job via `cron` scheduler
- Event sourcing for full audit trail per transaction
- Saga compensation for failed multi-step payment flows
- Load tested to **10,000 TPS** on 4 vCPUs with `k6`

<p>
<img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white">
<img src="https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apache-kafka&logoColor=white">
<img src="https://img.shields.io/badge/Stripe-008CDD?style=flat-square&logo=stripe&logoColor=white">
</p>

</td>
</tr>
</table>

---

## 📱 **The Mobile Arsenal: Native & Cross-Platform**

> 40+ production apps shipped across iOS, Android, and cross-platform — written in the language the platform deserves.

---

### 🍎 Native iOS · Swift

<table align="center" width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🏥 HEALIO · iOS</h3>
      <p align="center"><b>AI Telemedicine — Native Swift</b></p>
      <hr>
      <ul>
        <li>Built with <b>SwiftUI + Combine</b> reactive architecture</li>
        <li>WebRTC video consultations via native WebKit</li>
        <li>HealthKit vitals integration</li>
        <li>Core ML on-device symptom triage model</li>
        <li>Face ID / Touch ID authentication</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white">
        <img src="https://img.shields.io/badge/SwiftUI-0175C2?style=flat-square&logo=swift&logoColor=white">
        <img src="https://img.shields.io/badge/Core_ML-000000?style=flat-square&logo=apple&logoColor=white">
        <img src="https://img.shields.io/badge/HealthKit-FF2D55?style=flat-square&logo=apple&logoColor=white">
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">💳 VAULTPAY · iOS</h3>
      <p align="center"><b>Digital Wallet — Native Swift</b></p>
      <hr>
      <ul>
        <li>UIKit + Programmatic layouts (no storyboards)</li>
        <li>Apple Pay & Wallet integration</li>
        <li>Keychain Services for credential storage</li>
        <li>CryptoKit for client-side encryption</li>
        <li>Background sync via BGTaskScheduler</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white">
        <img src="https://img.shields.io/badge/UIKit-2396F3?style=flat-square&logo=apple&logoColor=white">
        <img src="https://img.shields.io/badge/CryptoKit-000000?style=flat-square&logo=apple&logoColor=white">
      </p>
    </td>
  </tr>
</table>

---

### 🤖 Native Android · Kotlin & Java

<table align="center" width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🚨 NEMA · Android</h3>
      <p align="center"><b>National Emergency System — Kotlin</b></p>
      <hr>
      <ul>
        <li>Jetpack Compose UI with Material 3</li>
        <li>Offline-first with Room DB + WorkManager sync</li>
        <li>Google Maps SDK — geospatial disaster tracking</li>
        <li>Foreground service for persistent location reporting</li>
        <li>Coroutines + Flow for reactive data pipelines</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Kotlin-0095D5?style=flat-square&logo=kotlin&logoColor=white">
        <img src="https://img.shields.io/badge/Jetpack_Compose-4285F4?style=flat-square&logo=android&logoColor=white">
        <img src="https://img.shields.io/badge/Room-3DDC84?style=flat-square&logo=android&logoColor=white">
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🏙️ PLENTI · Android</h3>
      <p align="center"><b>E-Commerce Superapp — Java/Kotlin</b></p>
      <hr>
      <ul>
        <li>Legacy Java core migrated incrementally to Kotlin</li>
        <li>MVVM + Repository + UseCases (clean arch)</li>
        <li>Paging 3 for 50,000+ SKU catalogue</li>
        <li>ExoPlayer for product video previews</li>
        <li>Firebase Cloud Messaging + in-app notifications</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Kotlin-0095D5?style=flat-square&logo=kotlin&logoColor=white">
        <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white">
        <img src="https://img.shields.io/badge/Paging_3-3DDC84?style=flat-square&logo=android&logoColor=white">
      </p>
    </td>
  </tr>
</table>

---

### 🎯 Cross-Platform · Dart / Flutter

<table align="center" width="100%">
  <tr>
    <td width="33%" valign="top">
      <h3 align="center">🏙️ PLENTI</h3>
      <p align="center"><b>Hyper-Scale E-Commerce</b></p>
      <hr>
      <ul>
        <li>50,000+ SKU catalogue</li>
        <li>Real-time cart sync</li>
        <li>Multi-gateway payments</li>
        <li>Live driver tracking</li>
        <li>Role-based access control</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white">
        <img src="https://img.shields.io/badge/Riverpod-2D3748?style=flat-square&logo=dart&logoColor=white">
        <img src="https://img.shields.io/badge/Go_Backend-00ADD8?style=flat-square&logo=go&logoColor=white">
      </p>
    </td>
    <td width="33%" valign="top">
      <h3 align="center">🏠 HOMEWIN</h3>
      <p align="center"><b>Gamified Real Estate</b></p>
      <hr>
      <ul>
        <li>Live lottery events</li>
        <li>Real-time bidding engine</li>
        <li>360° property tours</li>
        <li>Secure payment flows</li>
        <li>Referral & rewards</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white">
        <img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=white">
      </p>
    </td>
    <td width="33%" valign="top">
      <h3 align="center">💬 PULSELINK</h3>
      <p align="center"><b>Encrypted Messaging</b></p>
      <hr>
      <ul>
        <li>End-to-end encryption</li>
        <li>AI message summarization</li>
        <li>File sharing up to 2GB</li>
        <li>Voice & video calls</li>
        <li>Cross-platform sync</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white">
        <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white">
      </p>
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <h3 align="center">🩺 HEALIO</h3>
      <p align="center"><b>AI Telemedicine</b></p>
      <hr>
      <ul>
        <li>Gemini AI symptom checker</li>
        <li>WebRTC video consults</li>
        <li>IoT vitals integration</li>
        <li>Digital prescriptions</li>
        <li>Appointment scheduling</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white">
        <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=google&logoColor=white">
      </p>
    </td>
    <td width="33%" valign="top">
      <h3 align="center">🍔 CHOW</h3>
      <p align="center"><b>Food Delivery Platform</b></p>
      <hr>
      <ul>
        <li>Real-time driver tracking</li>
        <li>ML ETA predictions</li>
        <li>Smart dispatch engine</li>
        <li>Multiple payment options</li>
        <li>Rating & review system</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white">
        <img src="https://img.shields.io/badge/Mapbox-000000?style=flat-square&logo=mapbox&logoColor=white">
      </p>
    </td>
    <td width="33%" valign="top">
      <h3 align="center">📈 CRYPTOVAULT</h3>
      <p align="center"><b>Crypto Portfolio Manager</b></p>
      <hr>
      <ul>
        <li>WebSocket price streams</li>
        <li>120fps candlestick charts</li>
        <li>RSI/MACD indicators</li>
        <li>Portfolio analytics</li>
        <li>Multi-chain wallet support</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white">
        <img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socket.io&logoColor=white">
      </p>
    </td>
  </tr>
</table>

---

## 🧰 **Full Tech Stack**

<div align="center">

### **Backend & Systems**

![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![gRPC](https://img.shields.io/badge/gRPC-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)

### **Mobile — Native**

![Swift](https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white)
![SwiftUI](https://img.shields.io/badge/SwiftUI-0175C2?style=for-the-badge&logo=swift&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-0095D5?style=for-the-badge&logo=kotlin&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Jetpack Compose](https://img.shields.io/badge/Jetpack_Compose-4285F4?style=for-the-badge&logo=android&logoColor=white)

### **Mobile — Cross-Platform**

![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)
![Riverpod](https://img.shields.io/badge/Riverpod-2D3748?style=for-the-badge&logo=codesandbox&logoColor=white)
![BLoC](https://img.shields.io/badge/BLoC-0052CC?style=for-the-badge&logo=react&logoColor=white)

### **Infrastructure & Cloud**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

### **AI & ML**

![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

</div>

---

## 📊 **GitHub at a Glance**

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=davidcreated&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00D9FF&icon_color=00D9FF&text_color=FFFFFF&count_private=true" height="180" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=davidcreated&theme=tokyonight&hide_border=true&background=0D1117&currStreakNum=00D9FF&sideNums=00D9FF&ring=00D9FF&fire=FF6B6B&currStreakLabel=00D9FF" height="180" />
</div>

<br>

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=davidcreated&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00D9FF&text_color=FFFFFF&langs_count=10" width="55%" />
</div>

<br>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=davidcreated&bg_color=0D1117&color=00D9FF&line=00D9FF&point=FFFFFF&area=true&hide_border=true" width="100%" />
</div>

---

## 🏛️ **Engineering Standards**

| Principle | Standard |
| :--- | :--- |
| **Interfaces** | Accept interfaces, return structs. Always. |
| **Concurrency** | Channels for communication. Mutexes for state. Never both carelessly. |
| **Error Handling** | Errors are values. Wrap with context. Never swallow. |
| **Observability** | Structured logs, distributed traces, and metrics on every service boundary. |
| **Mobile Performance** | 60fps minimum. If it jitters, it ships as a bug. |
| **Type Safety** | 100%. Stringly-typed code is technical debt with a timer. |
| **Testing** | Unit → Integration → Load. Nothing hits prod untested. |
| **Documentation** | Self-documenting code. READMEs for every module, ADRs for every major decision. |

---

## 🧠 **Engineering Philosophy**

<div align="center">

> *"A distributed system is correct when you can reason about every failure mode before it happens.*
> *A mobile app is excellent when users never think about the developer.*
> *Write Go like you'll be paged at 3am for it."*

</div>

---

## ☕ **Beyond The Code**

- ⚙️ Currently deep in **Go distributed systems** — microservices, event sourcing, CQRS
- 📱 Still obsessed with **16ms frame budgets** and butter-smooth mobile UX
- 🤖 Experimenting with **AI agents + Go** for autonomous workflow automation
- 🏗️ Building systems that can be handed to a new team and understood in one afternoon
- ☕ Best debugging happens at 2am with cold brew and a hot `pprof` profile

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7928CA,50:00D9FF,100:0D1117&height=140&section=footer&text=Let%27s%20Build%20Something%20That%20Lasts&fontSize=28&fontColor=ffffff&animation=fadeIn" width="100%"/>
</div>

<p align="center">
  <b>Open to senior engineering roles, technical leadership, and ambitious distributed systems challenges.</b>
</p>

<p align="center">
  <a href="mailto:timifroberts@gmail.com">
    <img src="https://img.shields.io/badge/Let's%20Talk-timifroberts@gmail.com-00D9FF?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117" alt="Email">
  </a>
</p>
