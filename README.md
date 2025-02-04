# Active Reading Tool (ACRE Tool)

The **Active Reading Tool (ACRE Tool)** is a program designed to enhance engagement in reading by creating a unique interactive experience that resembles the interactivity of a video game, all within the format of a book.

## Requirements

For the ACRE Tool to function, it requires a **screenplay**. A screenplay is a `.screen` file written in Screen Language, which the ACRE engine executes. The program utilizes an architecture similar to how theater organizes its productions to execute the screenplay, involving:

- **A) Stage Manager**: Responsible for managing the intangible aspects (the story).
- **B) Props Manager**: Responsible for managing the tangible aspects (stage props, actors, sets, etc.).


## Prop Manager

The **Prop Manager** is responsible for all prop-related tasks, including the windows the user interacts with.

### Responsibilities

1. Read and break down the script to create a detailed props list.
2. Collaborate with the director, production designer, and art department to finalize prop requirements.
3. Attend production meetings and rehearsals.
4. Source props through purchasing, renting, or fabrication.
5. Manage the props budget and track expenses.
6. Supervise prop artisans, carpenters, and assistant prop managers.
7. Plan and assign labor and resources for prop acquisition and construction.
8. Provide stand-in items for early rehearsals.
9. Set up and manage props tables backstage.
10. Ensure actors have their props before going on stage.
11. Maintain prop continuity throughout the production.
12. Secure valuable props after each performance.
13. Coordinate the return of rented or borrowed items.
14. Organize prop storage between performances.
15. Manage the strike process for props at the end of the production.
16. Maintain an inventory of props and manage the props storage area.
17. Research historical accuracy of props for period productions.
18. Train actors on proper use of props when necessary.
19. Manage the transportation of props to and from the production site.
20. Organize the sale or disposal of props after the production ends.
21. Work with special effects and stunts departments for specific prop requirements.
22. Ensure props meet safety standards and regulations.
23. Maintain and repair props as needed throughout the production.
24. Create a "set and strike" schedule for props.
25. Coordinate with the set decorator to ensure cohesive visual aesthetics.
26. Oversee the creation of custom props when necessary.
27. Manage food styling for scenes involving food props.
28. Handle animals used as props (in some productions).
29. Maintain logical progression of props throughout the story (props breakdown).

---

## Stage Manager

The **Stage Manager** is responsible for the smooth operation of all activities on stage, serving as the main hub of communication between the director, actors, and technical crew.

### Responsibilities

1. Attend all rehearsals and performances.
2. Create and manage the master calendar for rehearsals, deadlines, and performances.
3. Coordinate auditions with the director.
4. Handle script distribution and collection.
5. Prepare cast and crew contact lists.
6. Tape out the set dimensions on the rehearsal floor.
7. Set up and clean the rehearsal and performance spaces.
8. Record the director's blocking and assist actors with it.
9. Take line notes and prompt actors when needed.
10. Manage rehearsal props and furniture.
11. Chair production meetings.
12. Develop preset lists and running order lists.
13. Organize backstage storage areas.
14. Write and distribute daily rehearsal, production meeting, and performance reports.
15. Facilitate communication between production staff, cast, and crew.
16. Record all technical cues in the prompt book.
17. Manage the production callboard.
18. Monitor actors' attendance and punctuality.
19. Coordinate technical and dress rehearsals.
20. Supervise technicians, deck hands, and board operators.
21. Organize and supervise special rehearsals (fight calls, dance combinations, etc.).
22. Call all cues during performances.
23. Create and maintain the prompt book (master copy of the script).
24. Work closely with the director during rehearsals.
25. Ensure the production runs smoothly and as the director intended.
26. Coordinate with designers and craftspeople.
27. Manage set changes and create furniture and prop plans.
28. Oversee the entire show during each performance.
29. Solve problems and answer questions for cast and crew.
30. Maintain safety protocols backstage.


PropManager is a class.

	Its CONSTRUCTOR takes no arguments and it builds an instace of PropManager by:
		DESIGNing a Table of instances of Prop (null_objects_table) WITH a New instance of a Table that CATALOGUES instances of Prop by USING a Word (prop.id); 
		DESIGNing a List of Objects (inventory_table) WITH a New instance of a Table that CATALOGUES Objects USING a Word (prop_id) and,
		DESIGNing a Table of Lists (prop_continuity_table) WITH a  containing two lists, catalogued by:
			`buffer_list`: a List of keywords `prop_id`,
			`cache_list`: a List of keywords `prop_id`.

	The function `nullify` takes a GenericObjectType type (object_class_arg) as a parameter, when executed it:
		DEFINES GenericObjectType instance (nullptr) TO Empty,
		VERIFIES if the classname has been added to the local Table (null_objects_table), if it has:
			SET GenericObjectType instance TO the instance of a null object located in local Table (null_object_table),
		HOWEVER, if the classname hasn't been added yet:
			SET the GenericObjectType (nullptr) TO an empty instance of a GenericObjectType,
			ADD the instance (nullptr), TO the local Table (null_objects_table),
		and finally RETURNS the GenericObjectType instance (nullptr).
			
    	The function `read_script` takes File object instace (script_file_arg) as a parameter; it then reads the script by:
    		VERIFYING the File Object instance (script_file_arg) is fit to use, and if it isn't the function will:
    			RAISE an error,
    			and EXIT the program urgently.

        	SETTING a List of Words (excerpt_list).
        
		#FOR each (line) in the script_file, the function:
			VERIFIES if the prop flag is set to true, because if it does the function will:
				a) VERIFY if the current line contains a token for creating a new prop, because if the line contains such token then the function:
					RAISES an error,
					and EXIT the program urgently;
				b) VERIFY if the current line contains a token for ending the creation of a new prop, because if the line contains such token then the function:
					SETS the prop flag to false,
					ADDS the new excerpt to excerpts_list,
					CLEANS the excerpt_list from all words,
					and CONTINUES to the next line;
				c) ONLY AFTER, the function will: 
					ADD the line to the excerpt_list,
					and CONTINUE to the next line;
					
		#For each (excerpt) in the excerpt_list, the function: 
			VERIFIES if the excerpt has all the data required to be turned into a prefab, and if it doesn't the function will:
				RAISE a warning,
				and CONTINUE to the next line;
			ONLY AFTER, the function will:
				FORMAT the data to resemble a prop prefab, (prefab),
				APPEND the List of Words (prefab) TO the Table of List of Words (inventory_table). 		
        
        The FUNCTION `generate_propbox` takes a Manager instance (manager_arg) as a parameter, it then generates a Propbox by:
        	DEFINING an instance of a Propbox (box) AS a New instance of a Propbox with the Manager instance (manager_arg) passed during construction;
        	
        	#FOR each List of Words (prop_prefab) in local Table (inventory_table):
        		DEFINE a Prop instance (tmp) AS a New instance of a Prop with the List of Words (prop_prefab) passed during construction,
        		APPEND the Prop instance (tmp) TO the Propbox instance (box)
        	
        	Once all is done, it RETURNS the instance of a Propbox (box).
        

	The FUNCTION `manual_update` takes a Propbox instance (pbox_param,) and a List of Words (spellscript_list_param) as parameters, it manually updates a Propbox by:
		VERIFYING if the Propbox instance (pbox_param) is empty, because if it is the function should:
			RAISE an Error,
			EXIT program urgently
		
		and #FOR each (spellscript) in the List of Words (spellscript_list_param):
			APPEND the spellscript to the Propbox instance (pbox_param)
		
		then EXECUTING local FUNCTION `verify_prop_qc` with the Propbox instance (pbox_param), as a parameter.
		
	The FUNCTION `generate_prop` takes two List of Words, (prefab_prop_arg) and (tag_list_arg) as a parameters, it generates a Prop by:
		CREATING an intance of Prop (tmp_prop) WITH a New instance of a Prop with the List of Words (tag_list_arg) passed as parameter during construction;
		EXECUTING local FUNCTION `build_prop` WITH Propbox instance (tmp_prop) as a parameter during construction.
		RETURNING the Prop instance (prefab_prop_arg)
		
	The FUNCTION `get_debugger`, grants access to a debugger by:
		GENERATING? a debugger and,
		RETURNING the debugger;

	The FUNCTION `prop_follows_qa` takes an instance of a Prop (prop_param) as a parameter, it verifies the prop follows quality assurance:
		VERIFYING the Prop param (prop_param) is not empty, because if it is the function should:
			RAISE a Warning, then
			RETURN No.
		GETTING the Prop instance's (prop_param) List of Words (prop_spellscripts),
		then #FOR EACH List of Words (spellscript) in the List of Words (prop_spellscript),
			VERIFY if the spellscript can be executed by the Prop instance (prop_param), because if it doesn't,
				RAISE a Warning, then
				RETURN No.
		and finally, RETURNING Yes.
		
	The FUNCTION `update_inventory` takes an [optional] Table of objects (additional_props_param), and it updates the inventory by:
		DESIGNING a List of Words (warning_log) before checking,
		#FOR EACH Object (prop_prefab) in the Table of List of Words (inventory_table) so that the function can:
			VERIFY Object (prop_prefab) contains the data needed to become an instance of a Prop, because if it doesn't the function needs to:
				RAISE a Warning and,
				APPEND the Warning message to List of Words (warning_log);
			VERIFY Object (prop_prefab) is healthy BY EXECUTING local FUNCTION `prop_follows_qa` expecting a Yes from it, because if it return No the function needs to:
				RAISE a Warning and,
				APPEND the Warning message to List of Words (warning_log);
		and finally RETURNING the List of Words (warning_log).

	The FUNCTION `provide_testing_props` provides testing props by:
		DESIGNING a List of Props (testing_props), then
		DESIGNING an instance of a Prop (new_prop) BY CREATING a new Object with an Object (prefab) as an argument, then
		#FOR EACH Object (prefab) in the Table of Objects (inventory_table) the function will:
			VERIFIES Object (prop_prefab) is healthy BY EXECUTING local FUNCTION `prop_follows_qa` expecting a Yes from it, because if it return No the function needs to:
				RAISE a Warning and,
				CONTINUE with the next Object (prefab);
			APPENDS the instance of the prop to the List of Props (testing_props); 
		finally it RETURNING a List of Prop instances (testing_props).
		
	The FUNCTION  `mantain_prop_continuity` takes an instance of a Prop (prop_param) and a Word (location_param) as parameters, the function mantains prop continuity by:
		SWITCHing depending of the Word (location_param); it switches to:
			VERIFY SWITCHing TO `buffer_list`:
				VERIFY if the instance of a Prop's (prop_param) [unique] Word (prop.id) IS IN the List of Words (prop_continuity_table.buffer_list), because if it is then we:
				RAISE a Warning and,
				KILL the FUNCTION lifecycle.
				HOWEVER, if the instances don't match:
					APPEND the [unique] Word (prop.id) TO the List of Words (prop_continuity_table.buffer_list) and
					KILL the FUNCTION lifecycle.
			VERIFY SWITCHing TO `cache_list`:
				VERIFY the instance of a Prop (prop_param) [unique] Word (prop.id) IS IN the List of Words (prop_continuity_table.buffer_list), because if it isn't then the function:
					RAISE a Warning and,
					KILL the FUNCTION lifecycle.
				HOWEVER, if the instances match, the function will:
					REMOVE the [unique] Word (prop.id) FROM the List of Words (prop_continuity_table.buffer_list),
					APPEND the [unique] Word (prop.id) TO the List of Words (prop_continuity_table.cache_list) and
					KILL the FUNCTION lifecycle.
				OTHERWISE,
					RAISE an Error and,
					KILL the FUNCTION lifecycle.
					
	The FUNCTION `easy_clean`, assures the data has been saved before calling the garbage collector of the programming language, this is achieved by going  
		#FOR EACH List of Words (prop_prefab) IN Table of Lists (inventory_table) then proceeding to
			TRY TO:
				EXECUTE LOCAL Function `maintain_inventory`,
				"SAVE" the instance of Prop before
				"PERFORM"ing additional pre-closing requirements and finally
				EXITing the PROGRAM gracefully. However, there is a
			CATCH; in the chance an Error type (UpdateError) occurs, the function would need to: 
					RAISE an Error and
					EXIT the PROGRAM urgently.
			[and the same types of errors should be catched for saving, performing and exiting the program...]

	
	The FUNCTION `generate_prop` takes a Word (prop_id_param) as sole parameter, and it generates an instance of a Prop by:
		VERIFYing if the local Table of Objects (inventory_table) has a key/value pair linked to the Word (prop_id_param) because if it does then it will:
			CREATE an instance of an Object WITH GET the Object FROM the local Table (inventory_table) using the Word (prop_id_param) as key then it will 
			TRY TO:
				DESIGN an instance of Prop (prop_foo), BY CREATING a NEW instance of Prop with the Object (prop_prefab) as argument and
				RETURN the instance of Prop (prop_foo). However, there is a 
			CATCH; in the case an Error type (DesignError) occurs, the function would need to:
				RAISE an Error and
				EXIT the PROGRAM urgently.

			
		
	The FUNCTION `is_prop_functional` takes an Object (prefab_param) as a sole parameter; it returns a yes or no answer to if the prop is functional by:
		VERIFYing the Object (prefab_param) that contains all the parts required by an instance of a Prop to be generated- if it does the function will,
			  RETURNs a positive. 
		OTHERWISE the program will be forced to,
			RETURN a negative.

   
       
