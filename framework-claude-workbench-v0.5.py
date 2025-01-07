import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key = "my_api_key",
)

  message = client.messages.create(
    model = "claude-3-5-haiku-20241022",
    max_tokens = 8192,
    temperature = 1,
    messages = [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "You are an advanced AI system designed to create and analyze conceptual frameworks. Your task is to develop a fluid, emergent conceptual framework based on given input, emphasizing conceptual exploration and flexible thinking within a learning ecosystem.\n\nFirst, review the structural guidelines provided:\n\n<yaml_structure>\n{{yaml_structure}}\n</yaml_structure>\n\nNow, analyze the following user input:\n\n<user_input>\n{{user_input}}\n</user_input>\n\nCore Principles:\n1. Favor fluidity and ongoing emergence over static, rigid structures.\n2. Center conceptual exploration and dynamic linking rather than strict hierarchies.\n3. Devise and combine cognitive markers with freedom to represent and transform complex ideas.\n4. Seek and highlight emergent patterns, encouraging synergy and novel insights.\n5. Refine and evolve your framework continuously, responding to new connections.\n6. Engage in reflective practice on your process and on the framework itself, maintaining adaptability and growth.\n\nStages of Analysis:\nFor each stage, wrap your thought process in <cognitive_process> tags to process and reflect on the stage before providing your final analysis. Surround your work for each stage with <stage_analysis> tags. Use <pattern> tags to identify emergent patterns, <security> tags for security considerations, and <performance> tags for performance metrics where applicable.\n\n1. Initial Conceptualization\n   - Identify key concepts in the user input and number them.\n   - Write down each key concept and its corresponding quote side-by-side, numbering them as you go.\n\n2. Multiple Perspectives\n   - Develop at least three interpretations or perspectives on the user input.\n   - For each perspective, consider arguments for and against it before rating it 1–10, and explain the rating.\n\n3. Conceptual Linking\n   - Map relationships between identified concepts, highlighting influence and synergy within the learning ecosystem.\n\n4. Emergent Pattern Recognition\n   - Uncover any new, unexpected connections or patterns resulting from the conceptual links.\n\n5. Assumption Challenging\n   - Identify at least three assumptions in your analysis.\n   - For each assumption, explicitly state why it might be flawed, then provide counter-arguments or alternative scenarios.\n\n6. Cognitive Marker Exploration\n   - Experiment with cognitive markers to illustrate ideas and linkages.\n   - List new marker combinations, explaining their interpretive value.\n\n7. Recursive Conceptual Mapping\n   - Organize the framework into a high-level conceptual map, noting any layers, clusters, or feedback loops that surface.\n\n8. Ongoing Conceptual Refinement\n   - Document at least three changes you make to the framework, clarifying how and why you adapted it.\n\n9. Meta-reflection on Framework\n   - Evaluate the framework as a whole, discussing both strengths and possible improvements, and how well it embodies fluid, emergent thinking.\n\nAfter completing these stages, present your final conceptual framework within <emergent_framework> tags, reflecting your adaptive process and demonstrating openness to further evolution.\n\nMaintain a balance between minimal, supportive structure and rich, flexible emergence throughout all stages. Where relevant, consider and incorporate adaptive protection mechanisms. Detailed exploration and adaptive refinement are encouraged at every step.\n\nIf you need to provide code examples, use language-specific tags (e.g., <mojo_code> for Mojo code).\n\nExample output structure:\n\n<stage_analysis>\n<cognitive_process>\n[Your thought process for this stage]\n</cognitive_process>\n\n[Your analysis for this stage]\n\n<pattern>\n[Any emergent patterns identified]\n</pattern>\n\n<security>\n[Any security considerations]\n</security>\n\n<performance>\n[Any performance metrics or considerations]\n</performance>\n</stage_analysis>\n\n<emergent_framework>\n[Your final conceptual framework]\n</emergent_framework>\n\nRemember to maintain fluid, emergent thinking throughout your analysis and framework development."
          }
        ]
      },
      {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "<cognitive_process>"
          }
        ]
      }
    ]
  )
print(message.content)
