# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that we should check if the output in the Python script is being appended correctly. They raised this question after observing the behavior of the script. The exact details of the code or the specific output in question are not mentioned in the comment.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that @joaomdmoura merge this.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool, along with parent agents. The tool should have the capability to kick off a crew, managed by a parent crew. This approach will facilitate hierarchical organization and task delegation within the tool.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that instead of using a pre-computed or generalized manager, it would be better to have more control over the management process. This would allow for a more customized approach to managing the specific task or project at hand.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that `human_input` is used to assess the generated response after a task is performed. While incorporating additional context during agent input may not be optimal, providing all necessary input during `crew.kickoff()` could be a better approach. This ensures that the agent has the required context before task*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: Vidit-Ostwal has suggested including context about the agents or tools a manager LLM can use in the context hints section. However, they believe adding a `manager_note` specifically for one agent may not be optimal due to the LLM's internal structure, where it functions as an agent. Additionally, they suggest that*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that changing the Docker port and ClickHouse port from 9000 to 9005 resolved the issue. They changed both the ports, and it worked successfully.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the root of the problem lies in the inability to use port 9000. This is because a security process is running on that port and cannot be terminated. As a result, they are unable to proceed with their current course of action.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested re-trying a command that failed due to an issue with the database being unavailable. The logs provided show that Redis and PostgreSQL are running, but clickhouse migrations have repeatedly failed due to the database being unavailable.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested updating the ports in the `docker-compose.yml` file to resolve the issue faced while running the containers. The ports for ClickHouse and MinIO have been updated, and the relevant environment variables have been adjusted accordingly. @Vidit-Ostwal has also mentioned that if the problem persists, the issue might be*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a solution for the failure of the crew due to the lack of the user role in the llm when called. They recommend adding feedback in the user role to address this issue. The provided code demonstrates the implementation of the agents, tasks, and crew configuration with*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that you are getting a BadRequestError when calling the litellm completion API because the contents field in the GenerateContentRequest is not specified. They have shared code snippets to demonstrate the issue and the error message. Additionally, they have confirmed that they are using LiteLLM version 1.60.2 and*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the port 9000, used by both ClickHouse and MinIO, is already in use by another system process. They have tried to change the port but believe it is also used internally. Additionally, they are unable to apply ClickHouse migrations due to a database unavailability issue, resulting*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the sample code examples for using embeddings in CrewAI, the parameter `model_name` is incorrectly named and should be replaced with `model`. This affects examples for Azure OpenAI, Google AI, Vertex AI, and Cohere embeddings.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested introducing a JSON format option for the output_log_file, which currently uses a .txt format. The JSON format would facilitate further analysis, partially addressing issue #1970. @Vidit-Ostwal is willing to contribute a pull request for this feature.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by adding a user message formatted by the `feedback` function. This change addresses a specific problem that was causing an issue within the system. By implementing this fix, the overall functionality of the system is expected to improve, resulting in a better*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue highlighted in issue #2067. The fix should resolve the problem associated with the issue.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue raised in #2023. This fix involves removing the CLI command for resetting memories and making appropriate documentation changes. @Vidit-Ostwal has indicated willingness to implement these additional changes if the proposed solution is deemed suitable.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue that was raised in issue #2030. The details of the fix and any relevant code examples are not provided in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support for saving logs in JSON format. Users can now set `output_log_file` to a file name when initializing `Crew` and set `save_as_json` to `True`. The saved JSON file will include an array of JSON events, making it easy to analyze and use.*

## ⭐ Starred Repositories
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
