<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,40:00ADD8,100:7928CA&height=280&section=header&text=David%20Paul%20Folorunsho-Roberts&fontSize=46&animation=fadeIn&fontColor=ffffff&desc=Senior%20Software%20Engineer%20%E2%80%A2%20Go%20%26%20Distributed%20Systems%20%E2%80%A2%20Mobile%20Architect&descAlign=50&descAlignY=73&descSize=17" width="100%"/>
</div>

<br>

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=20&duration=3500&pause=1000&color=00ADD8&center=true&vCenter=true&width=850&lines=Go+Engineer+%E2%80%A2+Distributed+Systems+%E2%80%A2+Mobile+Architect;Swift+%E2%80%A2+Kotlin+%E2%80%A2+KMP+%E2%80%A2+React+Native+%E2%80%A2+Flutter;Design+for+failure.+Optimize+for+humans.+Ship+for+impact.;40%2B+Apps+Shipped+%E2%80%A2+Millions+of+Users+Served" alt="Typing SVG" />
  </a>
</div>

<br>

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=davidcreated&style=for-the-badge&color=00ADD8&labelColor=0D1117" />
  <img src="https://img.shields.io/github/followers/davidcreated?style=for-the-badge&color=7928CA&labelColor=0D1117&label=Followers" />
  <img src="https://img.shields.io/badge/Stars%20Earned-112-FFD700?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117" />
  <img src="https://img.shields.io/badge/Apps%20Shipped-40%2B-00ADD8?style=for-the-badge&labelColor=0D1117" />
  <img src="https://img.shields.io/badge/Experience-6%2B%20Years-orange?style=for-the-badge&labelColor=0D1117" />
  <img src="https://img.shields.io/badge/United%20Kingdom-%F0%9F%87%AC%F0%9F%87%A7-white?style=for-the-badge&labelColor=0D1117" />
</div>

<br>

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

## The Engineer

<img align="right" alt="Engineering" width="360" src="https://raw.githubusercontent.com/devSouvik/devSouvik/master/gif3.gif">

I build two kinds of things that are genuinely hard to build well:

**Backend systems in Go** built to be distributed, fault tolerant, and designed to fail safely at scale. I work at the level of gRPC contracts, Kafka event topologies, idempotent payment flows, and zero downtime deployments.

**Mobile products that feel inevitable.** Native Swift on iOS, native Kotlin on Android, shared logic with Kotlin Multiplatform, React Native for speed, Flutter for fidelity. I don't pick one tool and stretch it everywhere. I pick the right one per context.

Currently engineering backend infrastructure at **@escrow-tech** and distributed mobile systems at **@Homewin-Nigeria-Ltd**. Previously shipped systems serving government agencies, national fintech platforms, and consumer apps used by hundreds of thousands of people.

<br clear="right"/>

<br>

### Where I Operate

<div align="center">

| Domain | What I Actually Do |
| :--- | :--- |
| **Go and Distributed Systems** | Microservices, gRPC, Kafka, event sourcing, saga patterns, idempotency, production grade |
| **Native iOS with Swift** | SwiftUI, UIKit, Combine, Core ML, HealthKit, CryptoKit, background processing |
| **Native Android with Kotlin and Java** | Jetpack Compose, Coroutines, Flow, Room, WorkManager, legacy Java migration |
| **Kotlin Multiplatform** | Shared business logic across iOS and Android from a single codebase |
| **React Native** | Cross platform consumer apps where iteration speed is the constraint |
| **Flutter and Dart** | Pixel perfect cross platform with complex animation and custom rendering |
| **Infrastructure** | Docker, Kubernetes, AWS, GCP, Prometheus, Grafana, OpenTelemetry |
| **AI Integration** | Gemini, OpenAI, LangChain embedded directly into production workflows |

</div>

---

## Flagship Work

<br>

<div align="center">

> **Engineered the mobile infrastructure for Nigeria's National Emergency Management Agency (NEMA)** — a government grade system deployed across 36 states, serving active federal command centers during disaster response operations. Offline first architecture, government grade encryption, real time geospatial coordination, and compatibility down to Android 5.0 for field deployment in remote areas.

</div>

<br>

---

## Go Powered Systems

> Distributed systems built in Go for correctness, concurrency, and scale. No frameworks. Just idiomatic Go, clean interfaces, and engineering that holds under pressure.

<br>

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3>🏗️ NEXUS-OMS</h3>
      <p><b>Distributed Order Management System</b></p>
      <p>A fully event driven order lifecycle system built on six independently deployable Go microservices. Each domain (orders, kitchen, payments, stock, and gateway) owns its data store and communicates exclusively through Kafka events and gRPC contracts.</p>
      <br>
      <b>Engineering decisions that mattered:</b>
      <ul>
        <li>Saga pattern with compensating transactions for distributed consistency</li>
        <li>Outbox pattern guaranteeing exactly once event delivery</li>
        <li>Structured logging via <b>slog</b>, distributed tracing via OpenTelemetry</li>
        <li>Graceful shutdown on every service, no lost in flight work on deploy</li>
        <li>Domain isolated PostgreSQL stores, no cross service database joins</li>
      </ul>
      <br>
      <p>
        <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
        <img src="https://img.shields.io/badge/gRPC-4285F4?style=flat-square&logo=google&logoColor=white">
        <img src="https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apache-kafka&logoColor=white">
        <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white">
        <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white">
        <img src="https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white">
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🔐 SENTINEL</h3>
      <p><b>High Throughput API Gateway</b></p>
      <p>A custom reverse proxy and authentication gateway written entirely in Go. Handles <b>50,000+ requests per second</b> at peak with under 2ms P99 latency. Stateless JWT validation, Redis backed rate limiting, and live configuration reloads via etcd. No restarts, no downtime.</p>
      <br>
      <b>Engineering decisions that mattered:</b>
      <ul>
        <li>Zero allocation hot path using <b>sync.Pool</b> for request contexts</li>
        <li>Hybrid token bucket and sliding window rate limiter per client</li>
        <li>Circuit breaker per upstream (Hystrix inspired, written from scratch)</li>
        <li>mTLS between all internal services</li>
        <li>Live route config reload via etcd watch, zero downtime config changes</li>
      </ul>
      <br>
      <p>
        <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
        <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white">
        <img src="https://img.shields.io/badge/etcd-419EDA?style=flat-square">
        <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white">
        <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white">
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>📡 STREAMCORE</h3>
      <p><b>Real Time Event Streaming Engine</b></p>
      <p>A self hosted pub/sub and WebSocket fan out platform built to replace third party streaming dependencies. Supports thousands of concurrent subscribers with persistent event logs, consumer group semantics, and backpressure handling, entirely within the Go ecosystem.</p>
      <br>
      <b>Engineering decisions that mattered:</b>
      <ul>
        <li>Goroutine per connection WebSocket hub bounded by <b>semaphore.Weighted</b></li>
        <li>Buffered channels with explicit drop policy for slow consumers</li>
        <li>Consumer group offset tracking in Redis, resumable on restart</li>
        <li>Horizontal scaling via consistent hashing for partition ownership</li>
        <li>Built in dead letter queue for unprocessable events</li>
      </ul>
      <br>
      <p>
        <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
        <img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socket.io&logoColor=white">
        <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white">
        <img src="https://img.shields.io/badge/RocksDB-0080FF?style=flat-square">
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>💳 PAYLANE</h3>
      <p><b>Fintech Payment Processing Engine</b></p>
      <p>An idempotent, multi gateway payment service routing across Paystack, Flutterwave, and Stripe with automated reconciliation, webhook delivery guarantees, and a double entry ledger model ensuring financial accuracy at every step.</p>
      <br>
      <b>Engineering decisions that mattered:</b>
      <ul>
        <li>Idempotency keys in Redis, double charge protection by design</li>
        <li>Webhook retry engine with exponential backoff and full jitter</li>
        <li>Provider routing based on live success rate telemetry</li>
        <li>Event sourcing for complete, immutable audit trail per transaction</li>
        <li>Saga compensation for failed multi step payment flows</li>
        <li>Load tested to <b>10,000 TPS</b> on 4 vCPUs using k6</li>
      </ul>
      <br>
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

## Mobile Arsenal

> Six platforms. One engineer. The right tool for the right problem, every time.

<br>

### 🍎 Native iOS with Swift

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">HEALIO · iOS</h3>
      <p align="center"><b>AI Telemedicine Platform</b></p>
      <hr>
      <ul>
        <li>SwiftUI + Combine reactive architecture, no UIKit dependency</li>
        <li>WebRTC video consultations via native AVFoundation stack</li>
        <li>Core ML on device symptom triage, inference runs offline</li>
        <li>HealthKit integration for live vitals ingestion</li>
        <li>Face ID and Touch ID with Keychain backed session tokens</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white">
        <img src="https://img.shields.io/badge/SwiftUI-0175C2?style=flat-square&logo=swift&logoColor=white">
        <img src="https://img.shields.io/badge/Core_ML-000000?style=flat-square&logo=apple&logoColor=white">
        <img src="https://img.shields.io/badge/HealthKit-FF2D55?style=flat-square&logo=apple&logoColor=white">
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">VAULTPAY · iOS</h3>
      <p align="center"><b>Digital Wallet</b></p>
      <hr>
      <ul>
        <li>UIKit with fully programmatic layouts, zero storyboards</li>
        <li>Apple Pay and Wallet passbook integration</li>
        <li>CryptoKit for client side AES-GCM transaction signing</li>
        <li>BGTaskScheduler for background ledger sync</li>
        <li>Biometric re-authentication on sensitive actions</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white">
        <img src="https://img.shields.io/badge/UIKit-2396F3?style=flat-square&logo=apple&logoColor=white">
        <img src="https://img.shields.io/badge/CryptoKit-000000?style=flat-square&logo=apple&logoColor=white">
        <img src="https://img.shields.io/badge/Apple_Pay-000000?style=flat-square&logo=apple&logoColor=white">
      </p>
    </td>
  </tr>
</table>

<br>

### 🤖 Native Android with Kotlin and Java

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">NEMA · Android</h3>
      <p align="center"><b>National Emergency System</b></p>
      <hr>
      <ul>
        <li>Jetpack Compose UI with Material 3, fully dark mode adaptive</li>
        <li>Offline first with Room DB + WorkManager background sync</li>
        <li>Foreground service for persistent location reporting in the field</li>
        <li>Google Maps SDK with custom geospatial disaster overlays</li>
        <li>Coroutines + Flow reactive pipelines throughout</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Kotlin-0095D5?style=flat-square&logo=kotlin&logoColor=white">
        <img src="https://img.shields.io/badge/Jetpack_Compose-4285F4?style=flat-square&logo=android&logoColor=white">
        <img src="https://img.shields.io/badge/Room-3DDC84?style=flat-square&logo=android&logoColor=white">
        <img src="https://img.shields.io/badge/WorkManager-3DDC84?style=flat-square&logo=android&logoColor=white">
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">PLENTI · Android</h3>
      <p align="center"><b>E Commerce Superapp, Java to Kotlin</b></p>
      <hr>
      <ul>
        <li>Legacy Java core progressively migrated to Kotlin, zero regressions</li>
        <li>MVVM + Repository + UseCases clean architecture</li>
        <li>Paging 3 for 50,000+ SKU catalogue with smooth infinite scroll</li>
        <li>ExoPlayer for in feed product video previews</li>
        <li>FCM push and in app notification centre</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Kotlin-0095D5?style=flat-square&logo=kotlin&logoColor=white">
        <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white">
        <img src="https://img.shields.io/badge/Paging_3-3DDC84?style=flat-square&logo=android&logoColor=white">
        <img src="https://img.shields.io/badge/ExoPlayer-3DDC84?style=flat-square&logo=android&logoColor=white">
      </p>
    </td>
  </tr>
</table>

<br>

### 🔗 Kotlin Multiplatform

<table width="100%">
  <tr>
    <td width="60%" valign="top">
      <h3 align="center">CONNECTR · KMP</h3>
      <p align="center"><b>Professional Networking with Shared Core</b></p>
      <hr>
      <p>Business logic, data models, repository layer, and network calls written once in Kotlin and shared across iOS and Android. Each platform retains its native UI. SwiftUI on iOS, Jetpack Compose on Android. The shared module enforces a single source of truth for domain behaviour.</p>
      <ul>
        <li>Ktor client for shared HTTP, no Retrofit, no Alamofire</li>
        <li>SQLDelight for shared local database schema and queries</li>
        <li>Kotlinx.Serialization for cross platform JSON handling</li>
        <li>Kotlin Coroutines bridged to Swift async/await via KMP-NativeCoroutines</li>
      </ul>
    </td>
    <td width="40%" valign="top">
      <br><br>
      <p align="center">
        <img src="https://img.shields.io/badge/Kotlin_Multiplatform-0095D5?style=flat-square&logo=kotlin&logoColor=white">
        <img src="https://img.shields.io/badge/Ktor-0095D5?style=flat-square&logo=kotlin&logoColor=white">
        <img src="https://img.shields.io/badge/SQLDelight-3DDC84?style=flat-square&logo=android&logoColor=white">
        <img src="https://img.shields.io/badge/SwiftUI-F05138?style=flat-square&logo=swift&logoColor=white">
        <img src="https://img.shields.io/badge/Jetpack_Compose-4285F4?style=flat-square&logo=android&logoColor=white">
      </p>
    </td>
  </tr>
</table>

<br>

### ⚛️ React Native

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">CHOW · React Native</h3>
      <p align="center"><b>Food Delivery Platform</b></p>
      <hr>
      <ul>
        <li>Real time driver tracking via WebSocket + Mapbox</li>
        <li>ML powered ETA prediction with live recalculation</li>
        <li>Native modules for background location (bridged to Kotlin and Swift)</li>
        <li>Optimized FlatList rendering for large restaurant catalogues</li>
        <li>Reanimated 3 for 60fps order status animations</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB">
        <img src="https://img.shields.io/badge/Mapbox-000000?style=flat-square&logo=mapbox&logoColor=white">
        <img src="https://img.shields.io/badge/Reanimated_3-20232A?style=flat-square&logo=react&logoColor=61DAFB">
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">STREAMIFY · React Native</h3>
      <p align="center"><b>Live Streaming Platform</b></p>
      <hr>
      <ul>
        <li>Low latency live streams via Agora SDK (native bridge)</li>
        <li>Real time chat with animated reactions at 60fps</li>
        <li>Tip and donation flow with Stripe payment sheet</li>
        <li>Stream analytics dashboard rendered with Victory Native</li>
        <li>Custom native camera module for stream initiation</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB">
        <img src="https://img.shields.io/badge/Agora-099DFD?style=flat-square">
        <img src="https://img.shields.io/badge/Stripe-008CDD?style=flat-square&logo=stripe&logoColor=white">
      </p>
    </td>
  </tr>
</table>

<br>

### 🎯 Flutter and Dart

<table width="100%">
  <tr>
    <td width="33%" valign="top">
      <h3 align="center">HOMEWIN</h3>
      <p align="center"><b>Gamified Real Estate</b></p>
      <hr>
      <ul>
        <li>Live lottery events with real time bidding</li>
        <li>360° property tours via custom renderer</li>
        <li>Referral engine with reward tracking</li>
        <li>Secure multi gateway payment flows</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white">
        <img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=white">
        <img src="https://img.shields.io/badge/Riverpod-2D3748?style=flat-square">
      </p>
    </td>
    <td width="33%" valign="top">
      <h3 align="center">CRYPTOVAULT</h3>
      <p align="center"><b>Crypto Portfolio Manager</b></p>
      <hr>
      <ul>
        <li>WebSocket price streams with 120fps charts</li>
        <li>RSI and MACD indicators on custom canvas</li>
        <li>Portfolio performance analytics</li>
        <li>Multi chain wallet support</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white">
        <img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socket.io&logoColor=white">
        <img src="https://img.shields.io/badge/BLoC-0052CC?style=flat-square">
      </p>
    </td>
    <td width="33%" valign="top">
      <h3 align="center">PULSELINK</h3>
      <p align="center"><b>Encrypted Messaging</b></p>
      <hr>
      <ul>
        <li>End to end encrypted messaging</li>
        <li>AI message summarisation</li>
        <li>File sharing up to 2GB</li>
        <li>Voice and video calls via WebRTC</li>
      </ul>
      <p align="center">
        <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white">
        <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white">
        <img src="https://img.shields.io/badge/Riverpod-2D3748?style=flat-square">
      </p>
    </td>
  </tr>
</table>

---

## Full Tech Stack

<div align="center">

### Backend and Systems

![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![gRPC](https://img.shields.io/badge/gRPC-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)

### Mobile Native

![Swift](https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white)
![SwiftUI](https://img.shields.io/badge/SwiftUI-0175C2?style=for-the-badge&logo=swift&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-0095D5?style=for-the-badge&logo=kotlin&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Jetpack Compose](https://img.shields.io/badge/Jetpack_Compose-4285F4?style=for-the-badge&logo=android&logoColor=white)

### Mobile Multiplatform and Cross Platform

![Kotlin Multiplatform](https://img.shields.io/badge/Kotlin_Multiplatform-0095D5?style=for-the-badge&logo=kotlin&logoColor=white)
![React Native](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)

### Infrastructure and Observability

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=for-the-badge&logo=opentelemetry&logoColor=white)

### AI and ML

![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Core ML](https://img.shields.io/badge/Core_ML-000000?style=for-the-badge&logo=apple&logoColor=white)

</div>

---

## GitHub at a Glance

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=davidcreated&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00ADD8&icon_color=00ADD8&text_color=FFFFFF&count_private=true" height="180"/>
  &nbsp;&nbsp;
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=davidcreated&theme=tokyonight&hide_border=true&background=0D1117&currStreakNum=00ADD8&sideNums=00ADD8&ring=00ADD8&fire=FF6B6B&currStreakLabel=00ADD8" height="180"/>
</div>

<br>

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=davidcreated&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00ADD8&text_color=FFFFFF&langs_count=10" width="52%"/>
</div>

<br>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=davidcreated&bg_color=0D1117&color=00ADD8&line=00ADD8&point=FFFFFF&area=true&hide_border=true" width="100%"/>
</div>

---

## Engineering Standards

<div align="center">

| Principle | The Standard |
| :--- | :--- |
| **Go Interfaces** | Accept interfaces. Return structs. Every time. |
| **Concurrency** | Channels for coordination. Mutexes for state. Never conflated. |
| **Error Handling** | Errors are values. Wrap with context. Never silently swallowed. |
| **Mobile Performance** | 60fps is the baseline. Jank ships as a bug, not a feature. |
| **Type Safety** | 100%. Stringly typed logic is debt with a fuse attached. |
| **Observability** | Structured logs, distributed traces, and metrics at every service boundary. |
| **Testing** | Unit to Integration to Load. Nothing reaches prod untested. |
| **Idempotency** | Every write operation that can be retried must be safe to retry. |

</div>

---

## Engineering Philosophy

<div align="center">

> *"A distributed system earns trust when you can reason about every failure mode before it happens.*
> *A mobile app earns users when they never have to think about the developer.*
> *Write Go like you will be paged for it at 3am, because you will be."*

</div>

---

## Beyond The Code

- ⚙️ Currently deep in Go microservices: event sourcing, CQRS, distributed transactions
- 📱 Still obsessed with 16ms frame budgets and the craft of native mobile UX
- 🔗 Exploring Kotlin Multiplatform as the future of shared mobile logic
- 🤖 Building AI augmented workflows in Go: LLM orchestration, agent pipelines
- 🏗️ If a new team can't understand a system in one afternoon, it's not done yet

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7928CA,50:00ADD8,100:0D1117&height=140&section=footer&text=Let%27s%20Build%20Something%20That%20Lasts&fontSize=28&fontColor=ffffff&animation=fadeIn" width="100%"/>
</div>

<br>

<p align="center">
  <b>Open to senior engineering roles, technical leadership, and hard distributed systems problems.</b>
</p>

<br>

<p align="center">
  <a href="mailto:timifroberts@gmail.com">
    <img src="https://img.shields.io/badge/Let%27s%20Talk-timifroberts%40gmail.com-00ADD8?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117">
  </a>
</p>
