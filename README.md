# Recent GitHub Activity for Vidit-Ostwal

## 📝 Recent Blogs
- [Training the Tokenizer](https://www.notion.so/207e478805d48090b34fcc5c8e8c3c01?v=207e478805d480cfac6c000ca3c80482) - *03-06-2025*
- [Self-Attention in Transformers](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *21-06-2025*
  - [Masked Self-Attention](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *25-06-2025*
- [Temperature in LLM](https://open.substack.com/pub/viditostwal/p/how-does-temperature-changes-the?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *10-07-2025*
- [KV Caching in Transformers](https://open.substack.com/pub/viditostwal/p/kv-key-value-cache-in-transformers?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *26-07-2025*
## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/pull/3225#issuecomment-3122360852) in [crewAIInc/crewAI] on 2025-07-26.
  > *AI Summary: @Vidit-Ostwal has suggested that additional code needs to be added to mem0_storage. This action is proposed to be completed after the current changes in pull request #3217 are merged. The emphasis is on ensuring that the necessary modifications to mem0_storage occur following the successful integration of the existing updates. This approach aims to maintain orderly development and prevent potential conflicts or issues arising from simultaneous changes. Overall, the timeline for further code updates hinges on the merging of the specified pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/3220#issuecomment-3117867007) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested that the reason for sending messages in the assistant role pertains to changes made in the software's version updates. Specifically, there was a modification in the `save` method that wasn't fully considered. While sending both user and assistant messages would be beneficial, the current framework only records the Agent's replies. The assertion is made that this behavior may have evolved from version 1 to version 2, coinciding with changes in the search functionality, which now incorporates filtering features instead of simpler queries.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/3220#issuecomment-3117651845) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested to confirm whether any important details have been overlooked in the discussion. This points to a willingness to cooperate and clarify any potential misunderstandings. The mention of another user implies a collaborative approach, aiming for thoroughness in addressing the topic at hand. The emphasis is on ensuring that all aspects are covered, demonstrating a commitment to thorough communication within the team.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/3217#issuecomment-3117611164) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested a plan to improve memory handling. First, the addition of memories with a specified identifier should not be discarded. Second, the class should be refactored to remove support for a specific user identifier, with a target deadline set for version 0.156.0 or by August 4, 2025, when the UserMemory class is expected to be eliminated. This plan outlines clear steps for maintaining and enhancing functionality while ensuring timely updates.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/3217#issuecomment-3117397218) in [crewAIInc/crewAI] on 2025-07-25.
  > *AI Summary: @Vidit-Ostwal has suggested that instead of processing only user messages, we could send both user and assistant messages to Mem0. This approach may enhance the interaction by providing a more comprehensive context for requests. It emphasizes the importance of capturing the entire dialogue to improve the response and maintain continuity within conversations. By including both messages, we can better cater to user needs and foster engaging interactions in future exchanges. This method could lead to more personalized and effective communication outcomes.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/3220) in [crewAIInc/crewAI]: [BUG] Mem0 Memory Save / Search Issue (2025-07-25).
  > *AI Summary: @Vidit-Ostwal has suggested discussing the Mem0 Save and Search Issue as User-Memory will be replaced in two weeks. The current scenario involves issues with sending messages as 'assistant' messages and problems related to searching with both user_id and agent_id. Proposed solutions include retaining agent_id, sending message lists for Mem0 requests, and using an OR block in the filter instead of AND when both user_id and agent_id are present. Additionally, user_id support may be dropped until the upcoming software version deadline.*
- Raised an [issue](https://github.com/mem0ai/mem0/issues/3215) in [mem0ai/mem0]: Memory not saving with `infer=False` (2025-07-24).
  > *AI Summary: @Vidit-Ostwal has suggested that there is a bug with Mem0 in a project involving CrewAI, as memory is not being saved when the parameter is set to 'infer=False'. The user expresses concern about potentially doing something incorrect, since the functionality works correctly when 'infer=True'. The comment raises a query about the expected behavior of the memory-saving feature under different parameter settings.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/3225) in [crewAIInc/crewAI]: Dropping User Memory (2025-07-26).
  > *AI Summary: @Vidit-Ostwal has suggested refactoring the class by removing user_id support until the specified version 0.156.0 or until the deadline of August 4, 2025. This emphasizes the importance of streamlining the code and indicates that the UserMemory class should be eliminated by this date. The suggestion promotes clarity and organization within the codebase by ensuring that outdated or unnecessary elements are removed in a timely manner. Thus, adherence to this plan will improve the overall quality of the project.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/3216) in [crewAIInc/crewAI]: Changed the default value in Mem0 config (2025-07-24).
  > *AI Summary: @Vidit-Ostwal has suggested that the `infer=False` setting is not functioning as expected, as it defaults to `True` instead. This indicates a potential issue with the implementation or configuration that needs addressing. Further investigation may be required to understand why the intended functionality is not achieved and to resolve the discrepancy between the expected and actual behavior. Attention from the development team is necessary to rectify this issue.*

## ⭐ Starred Repositories
No repositories starred recently.

## 🍴 Forked Repositories
No repositories forked recently.
