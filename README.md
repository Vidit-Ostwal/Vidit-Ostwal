# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested that it would be helpful if the entire code could be shared. This would provide a more comprehensive understanding of the project and its implementation.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that @ashishpatel26 try updating the package as the sessions may end prematurely due to an outdated package. @Vidit-Ostwal has confirmed that the sessions end smoothly for them.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might be specific to the user's case and could not be reproduced. They recommend checking the provided goals and description, or trying to get the output in a different format, such as JSON.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested confirming whether the file path where your crew is running is the same as the path in the terminal where you're executing `crewai reset-memories -a`. This ensures the command is executed in the correct directory.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested checking whether the observation made by @ninad-opsverse regarding the appendation of information to the Python output is valid.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that @joaomdmoura should merge the current pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool and setting up parent agents. The crew inside the tool can be managed by a parent crew. This will allow the tool to kick off a crew based on the commands from the parent crew. By implementing this, we can achieve*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that pre-computed or generalized managers may be available, but it would be advantageous to maintain control over such aspects within the code. This would allow for greater customization and flexibility in managing the desired behavior and functionality.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that the `human_input` function should be called after the task has been performed and used to gather feedback on the quality of the generated response. Adding additional input context during the crew execution is discouraged. Instead, all necessary inputs should be provided during the `crew.kickoff()` method.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that including context about the agents or tools available to the manager LLM is a good idea. However, they raise the concern that adding a `manager_note` specifically for the manager LLM may not be the best approach since it is essentially just another agent internally. Instead, they*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the crew fails for any user input because lite llm is not given the user role in the messages. They have provided a code snippet and a screenshot to illustrate the issue and have suggested adding feedback in the user role as a possible solution.*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: Vidit-Ostwal has suggested that when calling litellm with Google Studio API, there is an issue where a BadRequestError is raised with the message "* GenerateContentRequest.contents: contents is not specified\n". This error occurs when the contents field in the GenerateContentRequest is not specified. Vidit-Ostwal is using litellm version 1.60.2 and is*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested addressing a port conflict issue during Langfuse setup using Docker Compose. Specifically, port 9000, used by both Clickhouse and Minio, is already occupied. Changing the port externally may not resolve the issue as it is likely used internally as well. The commenter seeks assistance in identifying all*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the CrewAI documentation for embeddings samples should use `model` as the parameter instead of `model_name` to match the actual usage. This is recommended for the CrewAI documentation pages covering Azure OpenAI, Google AI, Vertex AI, and Cohere embeddings. The reason for this change is to align*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the output_log_file to enhance its parsability for analysis purposes. This would partially address issue #1970. They are willing to contribute a pull request for this improvement.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by adding a user message formatted by "feedback." This update addresses the issue that was previously reported.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested the inclusion of a fix for the issue highlighted in #2067. This modification aims to resolve the reported problem effectively.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue reported in #2023. Additionally, they recommend:

- Removing the CLI command for resetting memories
- Making documentation changes

@Vidit-Ostwal is available to implement these changes if the proposed solution is accepted.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that this change fixes the documentation issue raised in #2030. No further details or code snippets were provided in the comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. When initializing the crew, you can set output_log_file to True or provide a filename (e.g., "log.json") and enable save_as_json to True. This generates a .json file containing an array of JSON events, making it easier to parse and*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
