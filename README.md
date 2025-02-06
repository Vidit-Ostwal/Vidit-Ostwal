# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve potential conflicts.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio review the code and share their thoughts. @Vidit-Ostwal also asks if the functionality improves the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal suggests checking if the issue is related to the previous unit test PR made by @sahusiddharth.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the current approach may not be entirely clear and has proposed an alternative solution that they believe could be more effective. They have requested further clarification on the issue to ensure a better understanding of the problem at hand.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested feedback from @jjmachan and @dosu on the correctness of the provided solution.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that this unexpected behavior is likely caused by a specific condition in the code, specifically when the variance of the input tensors (var_x and var_y) is close to zero. They recommend checking if this condition is being met in the specific case and suggest re-scaling the input*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested modifying task 2 to eliminate explicit parameter setting. Instead, task 2 should be described as utilizing the output from task 1, without specifying specific parameters. This will resolve the issue where the error is raised due to the absence of the "detail" parameter in the input.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to use `{prompt_number} : {trace}` format. This will result in more readable traces of the form:
`{'prompt_1': {'name': 'claim_decomposition_prompt', 'input': ClaimDecompositionInput(response='Context'), 'output': ClaimDecompositionOutput(claims=['Output'])}`*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that the proposed solution aligns well with the user perspective, improving comprehensibility. From an implementation standpoint, it should be relatively straightforward to implement. @jjmachan's input is sought to confirm alignment, before incorporating the modification into the PR.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2015#issuecomment-2628794304) in [crewAIInc/crewAI] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the code for the feature. They believe it would be helpful for other users to refer to the implementation and contribute to the project.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the sample code examples given in the CrewAI documentation, the `model` parameter is used instead of the `model_name` parameter for the embedder input. This inconsistency affects examples using various embedding services including Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and Cohere Embeddings.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal suggests adding a JSON format to the output_log_file for enhanced parsing capabilities, partially addressing issue #1970. This feature enhances the core functionality of the logging mechanism, enabling more efficient analysis of log data. @Vidit-Ostwal expresses willingness to contribute a pull request implementing this improvement.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the purpose of `use_vision set = True` in defining an agent. They have observed that the output remains similar, with the only difference being the saving of a .gif file. To confirm whether multimodal image processing is occurring, they inquire about the availability of a cost*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030. Unfortunately, I am unable to provide any more details as the content of this comment is limited to 100 words.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. When initializing the crew, one can set output_log_file to True or provide a file name like "log.json", and enable save_as_json by setting it to True. Consequently, a .json file is generated containing an array of JSON events for*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the parse_run_traces function, which now includes the last four letters of the run_id for each trace. This modification results in a unique key for every call, ensuring that each trace is uniquely identifiable.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to specify the problematic indexed sample when an error occurs. This enhancement will provide more context and facilitate debugging, enabling developers to identify the specific sample causing the issue.*

## ⭐ Starred Repositories
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
