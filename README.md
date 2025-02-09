# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2644717512) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal has suggested resolving the issue by closing it if the PR fixes the problem. They believe that the PR should address the issues raised in the issue description.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2644714108) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal suggests that when yielding a particular value, it is converted to a generator object. To use the actual value, one must iterate through it. The provided code example demonstrates this process, where a function yields a city name that is then used in a subsequent function to retrieve a*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2055#issuecomment-2643704539) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may have been resolved. They recommend updating the crew version and provided a link to PR #2055 for further information.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2643616523) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: Vidit-Ostwal commends the contributions of @lorenzejay and highlights the missed opportunity of creating a `get_crew` functionality linked to a CLI command. Vidit-Ostwal also expresses interest in exploring the possibility of incorporating built-in evaluations for CrewAI, similar to RAGAS' structured evaluations for retrieval-augmented generation. This would enable assessments of tool outputs,*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal suggests expanding the current implementation to include a `get_crew` functionality. This would allow CLI commands to directly link with the current crew instance, enhancing usability and simplifying the workflow. The suggestion acknowledges the initial work done by @lorenzejay and aims to further improve the solution.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the problem may stem from discrepancies in initializing `short_term_memory` and `entity_memory` between the `reset_memory_command` executed from the CLI and the `crew.py` script. They point out that while the `reset_memory_command` works correctly for `long_term_memory` and `knowledge_memory`, it may not be suitable if custom initialization of any memory*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @jjmachan and @sahusiddharth to resolve any potential conflicts.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio review a specific code and provide feedback on its potential to enhance the user experience. @Vidit-Ostwal seeks @bhancockio's opinion on whether this functionality brings about a positive impact on the user's experience with the product or application.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that this issue might be related to a previous unit test PR by @sahusiddharth. They have asked if this possibility can be investigated.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the provided solution may not be clear and has requested more information to better understand the issue. Additionally, they have suggested an alternative approach that they believe should address the problem.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue where the port 9000 is used by multiple services, preventing langfuse setup via docker-compose. The issue arises due to port contention with an external system process. @Vidit-Ostwal has attempted to change the port but believes that other internal references to port 9000*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the CrewAI docs for memory usage, the embedder code examples should use the `model_name` parameter instead of `model`. This needs to be changed in the following sections: 1. Using Azure OpenAI Embeddings 2. Using Google AI Embeddings 3. Using Vertex AI Embeddings 4. Using Cohere*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON format support to the output_log_file for enhanced analysis capabilities. The current .txt format limits data usability. This modification partially addresses issue #1970. @Vidit-Ostwal is willing to contribute a pull request implementing this feature.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested checking the use of `use_vision set = True` in defining an agent. They are unsure of whether the screenshot goes to the multimodal LLM for phrasing or if the entire thing falls back to scraping elements and making decisions based on that. They have noticed that the*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the memory reset issue reported in issue #2023, including:

- Removal of the CLI reset memories command
- Necessary documentation updates

They have expressed willingness to implement these changes, pending confirmation that the proposed solution aligns with the project's goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that this commit fixes the documentation issue previously reported in issue #2030. The documentation has been updated and should now be accurate and helpful for users.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. Users can enable this feature by setting output_log_file to True or providing a file name. Additionally, save_as_json should be set to True. The resulting JSON file contains an array of JSON events, simplifying parsing and analysis.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a modification to the parse_run_traces function. This modification involves incorporating the last four characters of the run ID of the trace into the function. By implementing this change, each call will have a unique key, ensuring that the function can effectively differentiate between various calls. This modification*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples function to include information about the indexed sample that is causing an issue. This improvement provides more specific diagnostic information to help identify and resolve any issues with the samples.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
