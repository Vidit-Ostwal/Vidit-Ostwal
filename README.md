# Recent GitHub Activity for Vidit-Ostwal

## 📝 Recent Blogs
- [Training the Tokenizer](https://www.notion.so/207e478805d48090b34fcc5c8e8c3c01?v=207e478805d480cfac6c000ca3c80482) - *03-06-2025*
- [Self-Attention in Transformers](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *21-06-2025*
  - [Masked Self-Attention](https://www.notion.so/viditostwal/Self-Attention-in-Transformers-216e478805d48005b515fac90e1d76e0) - *25-06-2025*
- [Temperature in LLM](https://open.substack.com/pub/viditostwal/p/how-does-temperature-changes-the?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *10-07-2025*
- [KV Caching in Transformers](https://open.substack.com/pub/viditostwal/p/kv-key-value-cache-in-transformers?r=m52qu&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) - *26-07-2025*
## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2885#issuecomment-3585078738) in [crewAIInc/crewAI] on 2025-11-27.
  > *AI Summary: @Vidit-Ostwal has suggested verifying the functionality of calls to gpt-oss independently, without relying on crewai. Additionally, there is a question regarding whether the setup is self-hosted or cloud-hosted. This inquiry aims to clarify the nature of the hosting environment in use for gpt-oss, which is essential for understanding the context and dependencies involved in the system's operation. Such checks could ensure proper implementation and functionality of the service in question.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2885#issuecomment-3585054759) in [crewAIInc/crewAI] on 2025-11-27.
  > *AI Summary: @Vidit-Ostwal has suggested that an important parameter seems to be missing in the current implementation. Specifically, it is recommended to include the parameter `is_litellm = True` when defining the LLM object. Additionally, @Vidit-Ostwal inquires whether the performance drop observed applies to the qwen3 model as well. This highlights a potential oversight in the setup and a need for clarification regarding performance consistency across different models.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2885#issuecomment-3581146974) in [crewAIInc/crewAI] on 2025-11-26.
  > *AI Summary: @Vidit-Ostwal has suggested trying an installation command to address the issue. A recent change was made to relax certain conditions within the is_null_response_because_context_length_exceeded function. The purpose of this adjustment is likely aimed at improving functionality or resolving specific errors encountered previously. It is recommended to utilize the provided installation command to implement these modifications and test for better response handling. Please proceed with this suggestion to assess its effectiveness in resolving the issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2885#issuecomment-3580812387) in [crewAIInc/crewAI] on 2025-11-26.
  > *AI Summary: @Vidit-Ostwal has suggested checking the debug logs for specific indicators before a failure occurs. They pointed out two conditions to observe: whether the content length is exceeded, which should show as "is_content_length_excedded: False," and to verify if there is a null response due to context length not being exceeded, indicated by "is_null_response_becuase_context_length_exceeded: False." These checks may provide insights into the reasons behind the failure.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2885#issuecomment-3575388915) in [crewAIInc/crewAI] on 2025-11-25.
  > *AI Summary: @Vidit-Ostwal has suggested sharing traces and indicated that the system should typically retry with summarization. They mentioned the importance of verifying the `respect_context_window` parameter is set to `True`. Additionally, they pointed out that logs may show messages indicating the context length is exceeded, which leads to content summarization to fit the model's context window, suggesting it may take longer to process. This emphasizes the need for proper configuration to avoid issues during operation.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/3929) in [crewAIInc/crewAI]: [BUG] Task can't be configured when passing None as a context parameter via YAML (2025-11-16).
  > *AI Summary: @Vidit-Ostwal has suggested that an error occurs when attempting to execute a task with a context parameter set to None. The expected outcome should be a successful configuration without issues. The problem has been documented under the latest versions of macOS, Python, and crewAI, with evidence provided. Additionally, there are duplicates of this issue noted, indicating a need for attention to the identified bugs. A possible solution can be tracked in related issue references, emphasizing the ongoing challenge in the current environment setup.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/3845) in [crewAIInc/crewAI]: [BUG] LLMStreamChunkEvent has no differentiator (2025-11-06).
  > *AI Summary: @Vidit-Ostwal has suggested that while using FastAPI and Crewai, there is a problem identifying which streams correspond to the same message due to the absence of a message_id property in LLMStreamChunkEvent. Instead of relying on task_id and agent_id, which can lead to message merging when the same agent speaks twice, a definitive solution to this issue is sought. Insights based on the implementation of this feature would be appreciated to address the challenge effectively.*

## 🚀 Pull Requests
No pull requests opened recently.

## ⭐ Starred Repositories
No repositories starred recently.

## 🍴 Forked Repositories
- Forked [Vidit-Ostwal/verifiers](https://github.com/Vidit-Ostwal/verifiers) on 2025-10-29.
