# 動態多資產配置與微服務戰情室系統

## 資源與參考連結
- **[完整 Introduction (A. to F. 架構)]**: [docs/introduction_revised.md](docs/introduction_revised.md)
- **[完整 Related Work (文獻探討)]**: [docs/related_work.md](docs/related_work.md)
- **[對話紀錄 (Related Work 參考資料)]**: [Perplexity Search](https://www.perplexity.ai/search/2bf7eda8-7666-45d9-8312-b1abf824477f#14)
- **[簡報/規格書 Proposed Design]**: [Google Slides Presentation](https://docs.google.com/presentation/d/1TU4X4ZUnunU1NLg83RluyfNbQz_qsY_O/edit?usp=sharing&ouid=106316695064653404133&rtpof=true&sd=true)
- **[展示影片 Video Demo]**: [YouTube Video (10 minutes)](https://www.youtube.com/watch?v=0eg7N7yPJR4)

---

## 1. Introduction (A. to F. 摘要)
*(詳見：[完整版 Introduction](docs/introduction_revised.md))*

本研究提出一套整合**近端策略最佳化 (PPO)** 與**聰明錢概念 (SMC)** 的多資產動態配置框架，並透過微服務架構開發戰情室系統以確保決策透明度：
- **動機及引題 (Attention Getter & Motivation)**：量化市場與 AI 基礎設施高速發展，單純追逐高成長資產的風險同步升高。
- **挑戰 (But)**：傳統資產配置（如 Markowitz 模型）無法快速適應政經環境的結構性轉變 (Regime shift)，且大眾技術指標具有滯後性。
- **解藥 (Cure)**：將 SMC 的市場微觀結構概念精準量化，結合 PPO 動態配置優點以克服上述痛點。
- **方法設計 (Development)**：區分攻擊型、避險型與現金部位，採用 React + Spring Boot 微服務架構實作視覺化系統。
- **實驗 (Experiments)**：收集多年度歷史數據，評估年化報酬、最大回撤 (MDD) 與夏普比率等關鍵績效。
- **發現 (Findings)**：預期能有效實現風險移轉，兼具市場動態適應能力與金融科技工程落地可行性。

---

## 2. Related Work (文獻探討摘要)
*(詳見：[完整版 Related Work](docs/related_work.md))*

本研究的文獻基礎建構於四大面向，以突顯 PPO 與 SMC 結合之前瞻價值：
1. **傳統資產配置與其侷限性**：儘管奠定基礎，但在極端事件下其高回撤風險已不足以應對現代市場。
2. **深度強化學習於資產配置之發展**：PPO 已獲實證在投資組合中表現亮眼且報酬豐厚，但特徵設計較少著墨機構流動性。
3. **聰明錢概念 (SMC) 與市場結構量化之探討**：為解決傳統指標滯後所造成的風險，我們將實務上的 FVG、OB 等特徵補足並首度整合入 RL 觀測狀態中。
4. **AI 交易系統架構與微服務戰情室**：參考業界實務 (如系統解耦、Kafka 分析) 建構視覺化系統，有效消弭「AI 黑箱」的隱患。

---

## 3. Proposed Design / 規格書

本系統的具體設計與規格書已整理於專案簡報中，重點包含：
- **系統架構設計**：說明 AI 模型如何與行情資料、微服務叢集（Spring Boot）以及前端戰情室（React）解耦與交互。
- **特徵工程與強化學習模型**：展示如何將 SMC 指標（如 FVG 距離百分比, OB 觸碰狀態與 BOS/CHoCh）量化為 PPO 網絡的連續特徵空間，建立訓練環境。
- **展示與動態操作**：請觀看影片示範，涵蓋即時資產配置權重變化、淨值曲線、SMC 訊號標記以及操作流程。

> 📄 **[點此閱覽 Proposed Design 系統規格書與簡報](https://docs.google.com/presentation/d/1TU4X4ZUnunU1NLg83RluyfNbQz_qsY_O/edit?usp=sharing&ouid=106316695064653404133&rtpof=true&sd=true)**
> 🎥 **[點此觀看 10 分鐘提案與系統展示影片](https://www.youtube.com/watch?v=0eg7N7yPJR4)**
