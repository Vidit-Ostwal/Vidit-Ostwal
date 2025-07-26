# Recent GitHub Activity for Vidit-Ostwal

## 📝 Recent Blogs
- [Training the Tokenizer](https://www.notion.so/207e478805d48090b34fcc5c8e8c3c01?v=207e478805d480cfac6c000ca3c80482) - *03-06-2025*
- [Self-Attention in Transformers](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *21-06-2025*
  - [Masked Self-Attention](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *25-06-2025*
- [Temperature in LLM](https://open.substack.com/pub/viditostwal/p/how-does-temperature-changes-the?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *10-07-2025*
- [KV Caching in Transformers](https://open.substack.com/pub/viditostwal/p/kv-key-value-cache-in-transformers?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *26-07-2025*
## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/3220#issuecomment-3117867007) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested that the current message sending mechanism is limited to the assistant's replies, and questioned whether this has always been the case or if it changed in V2. The commenter notes changes in the `save` method but hasn't addressed the sending of exchanged messages yet. They believe that the transition from version 1 to version 2 has altered the search functionality, moving from simple string queries to a more complex filter system. This change impacts how user messages are retrieved and stored within the framework.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/3220#issuecomment-3117651845) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested to confirm if any important details are overlooked. The emphasis is on ensuring that the information provided is comprehensive and accurate. Additional context or clarification may be required to meet expectations or finalize a discussion. It would be beneficial to communicate any possible oversights or additional insights to enhance understanding and collaboration. Engaging in this dialogue can help ensure all critical aspects are captured effectively.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/3217#issuecomment-3117611164) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested a plan to address specific issues. First, it is important to fix the addition of memories when an agent ID is provided, ensuring it isn’t dropped. Additionally, there should be a refactor of the class to eliminate user ID support until the specified deadline of version 0.156.0 or August 4, 2025. This date marks the point at which the UserMemory class will be removed, signaling a significant update in functionality.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/3217#issuecomment-3117397218) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested that instead of handling messages separately, it may be more efficient to compile a list of both user and assistant messages and send this consolidated list to Mem0. This approach allows for streamlined communication and better organization of message data, which can enhance the processing capabilities of the application. The focus here is on effectively sharing relevant information to improve overall conversation handling between the user and the assistant.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/3217#issuecomment-3117367833) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested that removing the `user_id` from both external and legacy user memory would result in a loss of user-specific memory that persists across sessions. This loss would hinder the integration with the crew's contextual memory system, which was the primary purpose of implementing external memory instead of relying solely on `user_memory`. It highlights the importance of maintaining `user_id` for effective memory management across user interactions.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/3220) in [crewAIInc/crewAI]: [BUG] Mem0 Memory Save / Search Issue (2025-07-25).
  > *AI Summary: @Vidit-Ostwal has suggested discussing the Mem0 Save and Search Issue, emphasizing that the User-Memory will be phased out in two weeks. Key points include the current state where all messages are tagged only as 'assistant', and the absence of the agent_id parameter during Mem0 search requests. Proposed solutions involve retaining agent_id and fixing memory additions when it is provided, refactoring user_id support until the specified deadline, sending a list of messages instead of a final message, and altering the search filter to use an OR block for better results.*
- Raised an [issue](https://github.com/mem0ai/mem0/issues/3215) in [mem0ai/mem0]: Memory not saving with `infer=False` (2025-07-24).
  > *AI Summary: @Vidit-Ostwal has suggested that while working on a project with CrewAI using Mem0, there is an issue where no memory is saved when the infer parameter is set to false. They express uncertainty about potentially making a mistake since sending only the assistant message should ideally work. They highlight that the functionality works correctly with the infer parameter set to true. Therefore, further investigation may be needed to understand the underlying cause of the bug when infer is set to false.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/3216) in [crewAIInc/crewAI]: Changed the default value in Mem0 config (2025-07-24).
  > *AI Summary: @Vidit-Ostwal has suggested that the `infer=False` option is not functioning as intended, resulting in its default value being set to `True`. This issue may affect the expected behavior and outcomes in the associated operations. It appears that further investigation may be required to address this discrepancy and ensure that the functionality aligns with user expectations. The comment indicates a need for a resolution to this particular concern to enhance usability and performance.*

## ⭐ Starred Repositories
- Starred [OpenPipe/ART](https://github.com/OpenPipe/ART) on 2025-07-20.
- Starred [jlumbroso/passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp) on 2025-07-19.

## 🍴 Forked Repositories
No repositories forked recently.
