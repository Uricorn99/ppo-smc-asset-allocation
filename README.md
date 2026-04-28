# 動態多資產配置與微服務戰情室系統

## 資源連結
- **[簡報/規格書 Proposed Design]**: [Google Slides Presentation](https://docs.google.com/presentation/d/1TU4X4ZUnunU1NLg83RluyfNbQz_qsY_O/edit?usp=sharing&ouid=106316695064653404133&rtpof=true&sd=true)
- **[展示影片 Video Demo]**: [YouTube Video (10 minutes)](https://www.youtube.com/watch?v=0eg7N7yPJR4)

---

## 1. Introduction / A. to F.

隨著生成式人工智慧、高效能運算與金融科技的快速發展，量化交易與智慧投資已成為資本市場的重要核心。AI 與半導體板塊（如 NVIDIA, AMD, TSM 等）的持續成長帶來了高報酬潛力，但同時也伴隨著高估值與高波動風險。傳統資產配置模型（如均值–變異數模型、固定比例股債平衡或傳統技術指標如 RSI, MACD 等）在面對市場結構性變化與極端波動時，往往存在滯後性且無法及時避險。

為因應上述挑戰，本系統提出一套**結合近端策略最佳化（PPO）與聰明錢概念（SMC）的動態多資產配置方法，並搭配微服務戰情室系統**：
1. **攻擊型資產（Risk-On）**：追求超額報酬的 AI 與半導體核心標的。
2. **避險型資產（Risk-Off）**：黃金與長天期美債，在市場轉弱時降低投資組合風險。
3. **絕對安全部位（Safety）**：現金部位，當市場出現股、債、金同步承壓時控制最大回撤。

系統透過微服務架構整合 AI 運算引擎、Spring Boot API Gateway 與 React 高互動戰情室介面，實現動態配置、風險控制、決策透明與系統落地能力。

---

## 2. Related Work / NotebookLM

傳統資產配置研究在面臨市場結構轉變時常暴露於尾部風險，雖然部分研究導入了動態風險偏好與深度強化學習（DRL），但在特徵整合上仍有不少侷限。
1. **傳統資產配置與動態風險偏好**：多以聚合指標描述市場狀態，較少明確納入市場微結構與機構流動性資訊。
2. **深度強化學習（DRL）於資產配置**：廣泛採用 Actor-Critic 架構，近端策略最佳化（PPO）因其樣本效率與穩定性成為主流。DRL 雖在效能上超越傳統模型，但依賴的特徵多為價格或傳統指標。
3. **Smart Money Concepts (SMC)**：透過市場結構（BOS, CHoCh）、訂單塊（OB）與公平價值缺口（FVG）追蹤機構流動性蹤跡。現有應用多為單一標的或裁量交易，少有系統性量化為可供強化學習模型使用的狀態向量。
4. **AI 交易系統與微服務戰情室**：將策略引擎封裝為獨立服務，結合微服務架構與前端戰情室打造可視化的儀表板，解決了 AI 黑箱問題並提升決策可解釋性。

*(結合 NotebookLM 整理與文獻探討，本系統解決上述缺口，將 SMC 特徵量化並匯入 PPO 模型中，為跨資產動態配置提供全方位的解決方案。)*

---

## 3. Proposed Design / 規格書

本系統的具體設計與規格書已整理於專案簡報中，重點包含：
- **系統架構設計**：說明 AI 模型如何與行情資料、微服務叢集（Spring Boot）以及前端戰情室（React）解耦與交互。
- **特徵工程與強化學習模型**：展示如何將 SMC 指標（如 FVG 距離百分比, OB 觸碰狀態, BOS/CHoCh 方向與 VIX）量化為 PPO 網絡的連續特徵空間，建立獎勵機制並透過 Gymnasium 提供訓練與驗證環境。
- **展示與動態操作**：涵蓋即時資產配置權重變化、淨值曲線、SMC 訊號標記以及系統的整體操作流程。

> 📄 **[點此閱覽 Proposed Design 系統規格書與簡報](https://docs.google.com/presentation/d/1TU4X4ZUnunU1NLg83RluyfNbQz_qsY_O/edit?usp=sharing&ouid=106316695064653404133&rtpof=true&sd=true)**
> 🎥 **[點此觀看 10 分鐘提案與系統展示影片](https://www.youtube.com/watch?v=0eg7N7yPJR4)**
