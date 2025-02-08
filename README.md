# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2644717512) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal has suggested closing the issue if the PR resolves the issue raised by @heckfy88. They believe that the PR addresses the concerns raised in the issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2644714108) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal suggests that when using a generator to yield a value in a flow, it should be iterated to obtain the actual value. The example code demonstrates this by utilizing the langchain_google_genai and crewai libraries to generate a random city and a fun fact about that city. The flow yields*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2055#issuecomment-2643704539) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may have been resolved. They recommend updating the crew version and checking out PR #2055 for further details.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2643616523) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal suggests considering the addition of built-in evaluations for CrewAI's tool outputs, agent performance, and task results. These evaluations would assess performance based on criteria like factual accuracy. @Vidit-Ostwal highlights the work of RAGAS in structured evaluations for retrieval-augmented generation as an example and expresses interest in hearing thoughts on*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested expanding the `get_crew` functionality to work with their CLI commands. They had initially missed this idea, but now propose linking the CLI command directly to the current crew instance. They acknowledge the great work done by @lorenzejay and appreciate their collaboration.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may arise from the way `reset_memory_command` executed from the CLI initializes `short_term_memory` and `entity_memory`, differing from their initialization in `crew.py`. While `reset_memory_command` is suitable for `long_term_memory` and `knowledge_memory`, direct CLI commands may not work for custom memory initialization.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve potential conflicts in the code.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio reviews the provided code and provides feedback on whether the implemented functionality enhances the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal suggests that the issue being faced might be related to a previous unit test Pull Request made by @sahusiddharth. The original comment does not contain any additional information, such as what this issue is or what the PR's side effects were.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested providing more details as the provided information is insufficient for understanding. They believe that their suggested approach should work for the task.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested a bug in setting up LangFuse via Docker Compose. When using docker-compose up, the port 9000 used by ClickHouse and Minio is already occupied. Changing the port in the configuration doesn't resolve the issue, as the port is also used internally. The bug manifests as an error*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that there is a discrepancy in the provided sample code for using embeddings. The parameter named `model` is referenced in the code, while the documentation specifies it as `model_name`. This issue is observed across multiple languages and platforms, including Azure OpenAI, Google AI, Vertex AI, and Cohere*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested introducing a JSON format in the logging file to enhance parsability. This change would address the current limitation of a .txt format. Additionally, it partially resolves issue #1970. @Vidit-Ostwal expresses willingness to contribute by submitting a pull request.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested checking the impact of `use_vision` parameter in defining an agent. They noted that enabling this parameter saves a .gif but doesn't seem to affect the output. They question whether the multimodal LLM is used for parsing when `use_vision` is true, or if element scraping and decision-making based*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested addressing the memory reset issue raised in #2023. They propose additional changes:

1. Removing the CLI command for memory reset.
2. Updating the documentation accordingly.

@Vidit-Ostwal seeks confirmation that these changes align with the intended solution before implementing them.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue reported in issue #2030. This fix ensures that the documentation accurately reflects the functionality of the code and resolves any inconsistencies or inaccuracies that were previously present.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a feature to save logs as a JSON file. To use this feature, set `output_log_file` to `True` or a file name, and set `save_as_json` to `True` when initializing the `Crew` object. The generated JSON file will consist of an array of JSON events, providing a convenient*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the `parse_run_traces` function. The change involves including the last 4 letters of the `run_id` of the trace, resulting in a unique key for each function call. This modification ensures that each call has a distinct identifier for better tracking and analysis.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to indicate the specific indexed sample causing any issues. This enhancement provides more precise error information, enabling developers to quickly identify and resolve sample-related problems.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
