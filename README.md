# Recent GitHub Activity for Vidit-Ostwal

## 📝 Recent Blogs
- [Training the Tokenizer](https://www.notion.so/207e478805d48090b34fcc5c8e8c3c01?v=207e478805d480cfac6c000ca3c80482) - *03-06-2025*
- [Self-Attention in Transformers](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *21-06-2025*
  - [Masked Self-Attention](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *25-06-2025*
- [Temperature in LLM](https://open.substack.com/pub/viditostwal/p/how-does-temperature-changes-the?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *10-07-2025*
- [KV Caching in Transformers](https://open.substack.com/pub/viditostwal/p/kv-key-value-cache-in-transformers?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *26-07-2025*
## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/3220#issuecomment-3117867007) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested that the framework currently only sends and stores the Agent's replies, and there's a curiosity about whether this has always been the case or changed with V2. The current behavior differs from earlier setups where developers manually added user messages. Additionally, there were changes in search functionality from V1 to V2, moving from a simple string query to one that incorporates various filter features. This shift is important for understanding how message exchanges are handled in the new framework version.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/3220#issuecomment-3117651845) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested confirming whether any critical information has been overlooked. The comment indicates a collaborative approach, inviting feedback to ensure all necessary points are addressed. It emphasizes the importance of thoroughness and encourages engagement to clarify any potential gaps in understanding or communication. This openness to dialogue reflects a commitment to ensuring comprehensive coverage of the topic at hand, fostering a thorough and effective resolution of any issues that may arise during the discussion.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/3217#issuecomment-3117611164) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested a plan to address key issues. Firstly, the addition of memories when an identifier is provided should be corrected, ensuring it is not discarded. Secondly, a refactor of the relevant class is proposed, which includes the removal of user identifier support until a specified deadline of version 0.156.0 or August 4, 2025, when the UserMemory class will be eliminated. This approach aims to streamline functionality and improve future updates.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/3217#issuecomment-3117397218) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested that we can send both the user and assistant messages to Mem0. This approach involves compiling the list of messages and organizing them based on their roles. By doing so, we can effectively transmit the necessary data while ensuring that both sides of the conversation are represented. This method aims to enhance communication while maintaining context and clarity in the messaging system. It is a practical way to manage user interactions and the assistant's responses efficiently.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/3217#issuecomment-3117367833) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested that if the `user_id` is removed from both external memory and legacy user memory, it would eliminate the ability to maintain user-specific memory that lasts across sessions. This would hinder the integration of such memory with the crew’s contextual memory system, which was the original purpose for utilizing external memory instead of relying solely on `user_memory`. Preserving `user_id` is crucial for achieving the desired functionality and continuity in user experience.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/3220) in [crewAIInc/crewAI]: [BUG] Mem0 Memory Save / Search Issue (2025-07-25).
  > *AI Summary: @Vidit-Ostwal has suggested discussing the Mem0 Save and Search Issue following the planned transition from User-Memory to external memory. The current scenario reveals issues with how messages are tagged and searched, especially without the agent_id. Proposed solutions include retaining the agent_id while dropping user_id support until a set deadline and sending a list of messages for Mem0 requests. Additionally, the search logic should shift from an AND block to an OR block when both user_id and agent_id are present, as this would improve filtering efficiency. *
- Raised an [issue](https://github.com/mem0ai/mem0/issues/3215) in [mem0ai/mem0]: Memory not saving with `infer=False` (2025-07-24).
  > *AI Summary: @Vidit-Ostwal has suggested that while using Mem0 in a project involving CrewAI, there is an issue where no memory is being saved when the setting is `infer=False`. They raised a query about whether they might be doing something incorrect, as the memory saving works fine when `infer=True`. This indicates a potential bug that requires further investigation to correct the behavior when `infer=False` is utilized.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/3216) in [crewAIInc/crewAI]: Changed the default value in Mem0 config (2025-07-24).
  > *AI Summary: @Vidit-Ostwal has suggested that the `infer=False` setting is not functioning properly, and the default value appears to have reverted to `True`. This issue is significant as it impacts expected behavior. Further investigation into why this setting is not behaving as intended is necessary. It may require input from the development team to resolve this inconsistency and ensure that the functionality aligns with user expectations.*

## ⭐ Starred Repositories
- Starred [OpenPipe/ART](https://github.com/OpenPipe/ART) on 2025-07-20.

## 🍴 Forked Repositories
No repositories forked recently.
