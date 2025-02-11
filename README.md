# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested a solution to the issue, where they changed the ClickHouse port from 9000 to 9005, as well as adjusting the Docker port. This adjustment resolved the problem. They expressed gratitude to @Steffen911 for their assistance.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may stem from a security process running on port 9000, which prevents the program from being executed on that port. This security process cannot be terminated, so an alternative port should be used.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that you can refer to the provided logs to get more context about the issue. The logs indicate that the Redis server is starting and running successfully, along with other services like PostgreSQL, ClickHouse, and MinIO. However, there seem to be multiple failed attempts to apply ClickHouse*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has updated the `docker-compose.yml` file to resolve an issue where ports for ClickHouse and MinIO were conflicting. The updated file now specifies external ports 9009 and 9010 for ClickHouse and MinIO, respectively. @Vidit-Ostwal also mentioned that the problem may lie in another internal file.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2067#issuecomment-2646579129) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested a pull request that allows passing an instance of the `LLM` class to run the evaluations. This will address the issue where the `LLM` class was not accessible during the evaluation process. The pull request offers a solution by making the `LLM` class available during evaluations, enabling*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646469809) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be due to the `\n` character. He recommends replacing it with a comma or using triple double quotes (`"""`) instead of single double quotes. He suggests that these changes should resolve the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2014#issuecomment-2646308001) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested setting the `CREWAI_STORAGE_DIR` environment variable to specify a custom directory for storing Crew instances and memories. This ensures that Crew data is stored in the desired location, as specified in the `.env` configuration file. Additionally, it's mentioned that this approach allows for control over the location where*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646302061) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that there may be an error in the way arguments are being passed to the tool. To investigate this further, @Vidit-Ostwal requests that the entire code be shared.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2054#issuecomment-2646300138) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has requested that the complete code be shared in the comment section. It is unclear if the code is already available elsewhere, but they would like to have it conveniently accessible within the comment thread for easy reference.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2065#issuecomment-2646298829) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested exploring alternative search engine optimization (SEO) tools to replace Serper.dev. These alternatives should provide comprehensive features for keyword research, SERP analysis, and competitor tracking. It is crucial to ensure that the chosen tool aligns with the specific needs and goals of the project. Additionally, factors such as*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has identified a bug where an attempt to set up Langfuse through Docker Compose leads to a conflict due to port 9000 being occupied by another system process. This port is utilized by both ClickHouse and Minio, and the user is unable to terminate the interfering process. They suspect*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples in the CrewAI documentation for memory embedding should replace the `model` parameter with `model_name`. This is because the embedder takes the input of `model_name`, not `model`, as specified in the docs page. The change should be made across all examples, including those*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested a core functionality feature for the project. The current output_log_file has a .txt format, which is not parsable. They propose adding a JSON format to the logging file for further analysis. This partially addresses issue #1970. @Vidit-Ostwal expresses willingness to contribute a pull request.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested evaluating the use of `use_vision set = True` when defining an agent. They question whether screenshots are processed by the multimodal LLMs or if they still rely on web scraping and element analysis for decision-making. They note that they have only observed the creation of a .gif*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the issue highlighted in issue #2067 in this commit. Unfortunately, the specific details of the issue and the resolution have not been provided in this commit message.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested to implement the following changes to address the reset memories issue mentioned in #2023:

1. Remove the CLI command to reset memories.
2. Make necessary documentation updates.

@Vidit-Ostwal indicated that they can make the changes if the proposed solution is aligned with the project's goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030, updating the documentation to address the identified problem.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a feature that supports saving logs as a JSON file. Users can now initialize the crew with output_log_file set to True or a file name, and enable save_as_json by setting it to True. This feature generates a JSON file containing an array of JSON events, simplifying*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a change to parse_run_traces function in order to include the last four letters of the run_id of the trace. This change provides a unique key for every call, ensuring that each call can be easily identified and tracked. By incorporating this change, the function is enhanced to*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
