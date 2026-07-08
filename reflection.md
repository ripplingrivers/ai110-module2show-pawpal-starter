# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial system architecture focuses on separating data storage from scheduling logic. It features four primary classes:

1. **Pet**: A data class containing identification attributes (`name`, `species`).
2. **Task**: A data class storing care activity specifications (`title`, `duration_minutes`, `priority`).
3. **Owner**: A management class representing the user profile (`name`), tracking their associated `Pet` objects, and maintaining daily availability (`available_time_minutes`).
4. **Scheduler**: The core logic layer responsible for holding a pool of pending `Task` objects. It includes methods to add tasks (`add_task`), algorithmically sort and filter tasks based on time constraints (`generate_plan`), and produce logic summaries (`get_explanation`).

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

My initial design uses four classes: Pet and Task serve as basic data storage objects, Owner manages lists of pets and tracks global time availability constraints, and Scheduler acts as the standalone logic layer to sort and filter tasks. It seems like a good design, so I haven't made any changes yet. 


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The system checks for timeline boundary conflicts based on matching explicit clock timestamps rather than parsing sliding duration intervals. This lightweight approach keeps runtime computations exceptionally fast and keeps code maintainable while offering quick, digestible warnings to the user.


**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
My scheduler detects conflicts by checking for exact matching string timestamps instead of mapping out full overlapping time blocks (like a 30-minute task blocking out a whole time window).

- Why is that tradeoff reasonable for this scenario?
Since it's just a simple pet care app it keeps the code lightweight, fast, and easy to read. It gives the owner a quick, clean alert if they accidentally put two things down at the same time without overcomplicating the logic.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI to brainstorm how to connect the classes, generate the starting skeletons, and map out the trickier datetime operations for sorting and recurring tasks. I also used it to help me debug my code whenever I ran into issues or errors with the way it was functioning or occasionally syntax errors that I couldn't figure out how to fix. 

- What kinds of prompts or questions were most helpful?
Asking things like, "How should the Scheduler retrieve all tasks from the Owner's pets?" or asking what a clear, readable way to print out a nested tuple format in the terminal would be usually worked best for me. Sometimes I had to get more detailed as it responded, like asking what the purpose of specific lines were or if it would be easier to do it another way, but for the most part questions like the ones above were definitely helpful. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
When setting up chronological sorting, the AI suggested a complex key sorting logic using a tuple structure that gave me an AttributeError when I tested it because it forgot to unpack the inner object inside my task pairs. I had to work on the code myself to get rid of the error, but it worked out afterward. 

- How did you evaluate or verify what the AI suggested?
I ran `python main.py` in my terminal, and read the traceback error closely, then realized the lambda function was seeing a raw tuple instead of the task properties, so I just adjusted the indexing myself until it passed. 

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
With the assistance and advice of AI, I wrote automated tests to verify that marking a task complete works, adding a task increases the pet's list size, tasks sort chronologically, and duplicate timestamps trigger system warnings. 

- Why were these tests important?
The things I was testing are the core features of the backend. Testing them makes sure that any changes to the UI in the future won't secretly break the scheduling engine, which is really important.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I think I'm pretty confident. The automated pytests passed perfectly green and the terminal logs match exactly what I expect. As far as I can tell, it does exactly what I want it to. 

- What edge cases would you test next if you had more time?
If I had more time, maybe I would test what happens if an owner enters an invalid time string format (like text instead of numbers) or what happens if a pet has zero tasks assigned to them. They're not very big things, but I think it would be nice to have that figured out as well. 

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I think I'm most satisfied with seeing the whole system connect end-to-end. Getting the automated logic from `pawpal_system.py` to seamlessly save data and show warning alerts live on the Streamlit web dashboard was really cool to see, just knowing that I was able to make a page like that is kind of exciting. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I did another iteration, I guess I would try to expand the conflict detection so it actually looks at task durations. That way, if a walk takes 60 minutes, the app would warn you if you try to schedule a feeding 15 minutes later. It sounds like an interesting idea, and something that would be needed to actually work as a good scheduling app. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
I think that the biggest thing I learned is that being the "lead architect" means planning out clean relationships between your objects before you type any code. If your class structure makes sense up front, collaborating with an AI assistant becomes way faster and it's much easier to debug when things go wrong. It's kind of hard keeping track of everything, but it resulted in a really nice end product I think, so I guess it's worth it. 

