# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2780728915) in [crewAIInc/crewAI] on 2025-04-05.
  > *AI Summary: Vidit-Ostwal has suggested that when initializing the `MDXSearchTool`, a `config` parameter should be passed. This configuration parameter is a dictionary containing settings for the language model and embedder. The language model configuration includes specifying the provider, such as "ollama", along with its specific model and optional parameters. Similarly, the embedder*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2024#issuecomment-2779235679) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested a comprehensive approach to enhance documentation clarity and contributor engagement. The suggestion involves updating documentation, particularly focusing on areas that lack sufficient information. This includes revising existing documentation to ensure accuracy, providing practical examples, and simplifying explanations. Furthermore, a roadmap for future documentation updates is recommended. They*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2779055100) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested initializing each language model (LLM), with a tip to initialize one and assign the same LLM to others for efficiency. They explained the choice of OpenAI as the default LLM, citing its early adoption and widespread compatibility, with other companies designing their APIs to work similarly. This*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2778410185) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested that users can define their own Language Model and pass it using the 'llm' parameter within the crew. This offers flexibility in choosing and configuring the desired language model for specific tasks. An example is provided, demonstrating how to initialize the LLM object with parameters such as*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2776559533) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested following up on the implementation. The query pertains to whether a proposed solution or method was effective for the intended user. The comment seeks confirmation regarding the successful application of a previously discussed approach. The essence of the message lies in soliciting feedback on the practical outcome*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2101#issuecomment-2776553749) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: @Vidit-Ostwal has suggested a potential solution to an issue. The suggestion involves upgrading the version of a particular software or library. The user experiencing the problem should attempt to update to the latest version and then re-test the functionality that was previously failing. This upgrade may contain bug fixes or*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2776524457) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested that the problem might be related to prompt engineering and proposes providing the large language model with more information about the tool. Vidit-Ostwal recommends replacing a specific function in the base_tool.py file. This function aims to enhance the tool's description by including details such as arguments, data*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773146947) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific large language model (LLM) being utilized. They mentioned testing the scenario with Gemini and reported that the issue in question was not observed during their experimentation. Therefore, understanding which LLM is being used is crucial for further analysis and troubleshooting, as different models*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773137518) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a method for viewing the prompt sent to the language model (LLM) because utilizing verbose mode does not provide sufficient information. To achieve this, they added a print statement within the `crew_agent_executor.py` file. Specifically, the print statement captures and displays the list of messages that are about*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773121476) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a detailed prompt for an AI assistant designed to find information about people. The prompt defines the assistant's role as a "People Information Specialist" with the goal of analyzing questions and using tools to search for individuals. It outlines the assistant's limitations, specifying that it can only*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: @Vidit-Ostwal has suggested implementing a feature to incorporate runtime data from Human through the Command Line Interface. This enhancement aims to facilitate a more dynamic and interactive user experience by enabling real-time data integration. The initial implementation focuses on establishing a foundational framework for data input. Future development plans involve*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case related to issue #2260. The test case aims to address a specific scenario involving the `validate` method. This addition is intended to improve the overall testing coverage and ensure the robustness of the `validate` function in handling various input conditions. The new test*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2448, focusing on improving user memory configuration within the Crew class. The original code was deemed inefficient due to redundant checks. The revised implementation streamlines the configuration process by primarily verifying the presence of `memory_config`. Instead of raising a TypeError, the updated logic*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, which arises when using tools within a crew via the `crewai run` CLI command. This process creates a virtual environment that incorrectly identifies `crewai_tools` as an optional dependency. To resolve this, Vidit-Ostwal proposes ensuring that `crewai_tools` is consistently installed, irrespective of whether*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: @Vidit-Ostwal has suggested building upon the changes introduced in pull request #2422. The focus of this update is to refine the existing codebase by eliminating a test case deemed unnecessary. This modification aims to streamline the testing process, potentially improving efficiency and reducing redundancy. The removal of the test case*

## ⭐ Starred Repositories
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
