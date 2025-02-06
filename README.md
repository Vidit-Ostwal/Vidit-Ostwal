# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve potential conflicts.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio review their code and provide feedback. They have also asked for an opinion on whether the code's functionality would enhance the user's experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might be related to the previous unit test PR by @sahusiddharth. They have requested them to check if there is any connection between the two.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested providing more context and details on the issue being faced. They believe that elaborating on the problem would enable a better understanding and resolution.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has inquired about the correctness of the proposed solution. They have reached out to @jjmachan and @dosu seeking their feedback and validation.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior observed is likely due to the specific input tensors used. They identified that the condition `(var_x < bound).any() or (var_y < bound).any()` is being hit, which triggers a warning about instability in calculations due to near-zero variance in the input data. They have*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the error in the `interpolate_inputs_and_add_conversation_history()` function is due to the absence of the `detail` parameter. They recommend modifying the code to add the parameter description to `task 2` without specifying the parameter itself. Instead, the description should indicate that the task should use the output from*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested an update to the traces functionality in the latest commit. The new traces will display `{prompt_number} : {trace}`. For instance, `{'prompt_1': {...}, 'prompt_2': {...}, 'prompt_3': {...}, 'prompt_4': {...}}`. This update provides a clearer and more organized representation of the traces.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested considering the user's perspective when making design decisions, as it improves usability and understanding. Implementing this change is deemed feasible and straightforward. @jjmachan's input will be sought before updating the PR to incorporate this modification.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2015#issuecomment-2628794304) in [crewAIInc/crewAI] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that @thinkcybercloud share the code for this issue in a comment.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the documentation for the "Memory" concept needs to be updated to reflect that the input parameter for embedder should be `model_name` instead of `model`. This applies to all the code examples provided in the documentation.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested the creation of a core feature that enhances the logging file's functionality. They propose adding a JSON format option to the currently available .txt format. This addition will allow for easier parsing and support further analysis. The proposed feature partially addresses issue #1970. They express their willingness*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the purpose of `use_vision set = True` when defining an agent. The commenter is unsure whether it triggers multimodal processing of images or simply saves a GIF. They also request a cost metric to ascertain whether multimodal image processing is occurring. Additionally, the commenter mentions that*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested addressing the documentation issue reported in issue #2030. They have not provided specific details about the issue or the resolution, leaving the exact nature of the fix to be determined through further investigation of the issue itself.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. This feature enables users to set output_log_file to True or provide a file name and set save_as_json to True during crew initialization. The generated JSON file contains an array of JSON events, providing an easy and structured way*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested changing the `parse_run_traces` function to include the last four letters of the run ID for each trace. This change ensures that each call has a unique key, likely to improve the accuracy and efficiency of the function.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested altering the validate_samples function. The updated function can now identify and report the particular indexed sample responsible for any issues encountered during sample validation. This improved functionality enhances the precision of error reporting, aiding in the efficient resolution of validation-related problems.*

## ⭐ Starred Repositories
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
