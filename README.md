# Recent GitHub Activity for Vidit-Ostwal

## 📝 Recent Blogs
- [Training the Tokenizer](https://www.notion.so/207e478805d48090b34fcc5c8e8c3c01?v=207e478805d480cfac6c000ca3c80482) - *03-06-2025*
- [Self-Attention in Transformers](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *21-06-2025*
  - [Masked Self-Attention](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *25-06-2025*
- [Temperature in LLM](https://open.substack.com/pub/viditostwal/p/how-does-temperature-changes-the?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *10-07-2025*
- [KV Caching in Transformers](https://open.substack.com/pub/viditostwal/p/kv-key-value-cache-in-transformers?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *26-07-2025*
## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/pull/3390#issuecomment-3217132293) in [crewAIInc/crewAI] on 2025-08-23.
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue identified in the project, specifically regarding problem #3391. The proposed solution aims to address the underlying concerns effectively, ensuring that the functionality is restored or improved. This fix is anticipated to enhance the overall performance and user experience of the application. It is important for all contributors to review and test the suggested changes thoroughly to confirm they solve the stated problem satisfactorily and integrate seamlessly into the existing codebase.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/3185#issuecomment-3216682728) in [crewAIInc/crewAI] on 2025-08-23.
  > *AI Summary: @Vidit-Ostwal has suggested that the situation where CrewOutput is instantiated without task_outputs should not occur, based on observations of the code. They emphasize the importance of confirming this observation with a maintainer to ensure accuracy and obtain a second opinion. This highlights the need for thorough review and collaboration in the development process to avoid potential issues related to code implementation. Overall, the comment underscores the significance of validating assumptions with team members.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/3185#issuecomment-3216270555) in [crewAIInc/crewAI] on 2025-08-23.
  > *AI Summary: @Vidit-Ostwal has suggested that when writing tests for the agent workflow, skipping the test case where CrewOutput is instantiated without task_outputs could be beneficial since it appears that scenario is not expected. Additionally, @Vidit-Ostwal has expressed confusion regarding the differing requirements for creating a CrewOutput object directly versus through the crew.kickoff() method. It is suggested that better error handling could be incorporated within the CrewOutput class itself, proposing that it raise an error if no TaskOutput is present.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2885#issuecomment-3216179723) in [crewAIInc/crewAI] on 2025-08-23.
  > *AI Summary: @Vidit-Ostwal has suggested debugging the issue and requested the sharing of the project file along with the implementation details of the tools used. This collaboration aims to better understand the problem and facilitate effective troubleshooting. By examining the shared resources, it will become easier to identify potential bugs and propose viable solutions. The suggestion emphasizes the importance of sharing relevant information to enhance the debugging process and collective efforts in problem-solving.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/3169#issuecomment-3214365725) in [crewAIInc/crewAI] on 2025-08-22.
  > *AI Summary: @Vidit-Ostwal has suggested saving a unique file in the project and requested the relevant embedder. They noted that knowledge sources may be chunked and retrieved, typically using OpenAI models, which necessitate an OpenAI key. However, since a different model is utilized, they requested either to provide the OpenAI key or to set up the required embedder function within the project. This adjustment is essential for proper functionality and integration of the embedding processes.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/3391) in [crewAIInc/crewAI]: [BUG] Mem0 Storage metadata limit breach (2025-08-23).
  > *AI Summary: @Vidit-Ostwal has suggested that when using External Memory with Mem0, save requests may fail if the metadata exceeds 2000 characters due to the inclusion of assistant messages, user messages, and system prompts. To reproduce this issue, users should generate responses longer than 2000 characters while using external memory. The expected behavior is for the process to work seamlessly without errors. Additional context and a possible solution have been identified, with relevant technical details about the operating system, Python version, and environment configuration noted.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/3390) in [crewAIInc/crewAI]: Adding user_interaction and agent_interaction directly from messages (2025-08-23).
  > *AI Summary: @Vidit-Ostwal has suggested changes to the pull request, indicating that user_message and agent_message should be included in the message during the save method call of Mem0 Storage, rather than in the metadata. Additionally, the messages parameter has been removed from the metadata configuration due to a character limitation of 2000. These adjustments aim to streamline the process and enhance functionality while remaining within the defined constraints of metadata.*

## ⭐ Starred Repositories
- Starred [willccbb/verifiers](https://github.com/willccbb/verifiers) on 2025-08-24.
- Starred [ByteDance-Seed/seed-oss](https://github.com/ByteDance-Seed/seed-oss) on 2025-08-22.

## 🍴 Forked Repositories
- Forked [github/github-mcp-server](https://github.com/Vidit-Ostwal/github-mcp-server) on 2025-08-24.
- Forked [google-gemini/gemini-cli](https://github.com/Vidit-Ostwal/gemini-cli) on 2025-08-23.
