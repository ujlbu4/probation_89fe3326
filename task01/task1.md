
### Task 1

Imagine the following situation: you are joining a cross-functional team which builds a front-end application using REST APIs. You are a first QA engineer and need to establish a QA process in the team.
1. What would you do in your first few days of work? Where would you start?
2. Which process would you establish around testing new functionality?
3. Which techniques or best practices in terms of code architecture and test design would you use in your automated tests?



##### Possible Approaches

Usually when I join a new team or project I try to define the current situation. At first there are two essential things, first one is to define goals and other requirements for this project, second one is to have a meeting with each member and stakeholder to recognize their expectations, attitudes, experience and other flavors. 


###### Define the goals

At first it's great to recognize what stakeholders expects from this project and what problem it solves. When this is clear to you it is easier to prioritise things and decisions, because you should always considering costs and benefits comparison. 

It's great to realize risks for this project, how they vary from minor to catastrophic and how likely they can occur. 
Depends on criticality you can better plan implementation and maintenance cost of qa processes decisions. 

Because in some rare cases the best approach would be just once manual test implemented solution and that it. For example in case when you have really tight deadlines, single-day project and not expected to extend it in a future (some landing page for specific conference or something like this)

So it's great to define the goals :)

###### Explore the project

Before to start to run in any direction it's essential to realize where you are and what you have. 

We need to understand what do have in next sections: 
- functional requirements
- non-functional requirements
- architecture and integration components
- infrastructure
- team
- current processes

Functional reqs are unique for every feature, the main thing (for now) with them is to define the current approaches how it collects and stores. Later we will decide if we need special tools for reqs or more lightweight tools would be fine. 

Non-functional reqs will help us to understand if we need more complex scenarios, tests or processes. For example do we need performance/load, fault-tolerant, security and other types of *-ility testing.

If a project already exists it is required to understand current architecture, it will help to define test levels and critical paths for testing. 

It's better to know what we have from infrastructure perspectives. Is it cloud solutions or our own servers. How do we configure stands — by hands or with provisioning tools. Do our engineers be ready to support and extend this. Do we have common tools for monitoring and deployments. And so on. 

It is essential to speak individually with each member of a team to better know his or her tech background, what tools he or she prefer, their opinion about tests, test coverage, do they have any struggles with the current process and so on. It will help to choose the best approach to implement new stuff or change some if it will require. 

And of course it is important to research current processes and make notes if there any downsides with them. 


-----
Upper-level Action plan usually looks likes as follow: 
- define the goals
- explore the project
  - functional requirements
  - non-functional requirements
  - architecture and integration components
  - infrastructure
  - team
  - current processes
- relationship with team members
  - developers
  - management / stakeholders
  - other qa engineers
- prepare a roadmap 
  - share with team and management
- QA
  - quality metrics
  - testing levels
  - functional requirements
  - processes
  - release management
  - ci/cd
  - infrastructure as a code
  - monitoring


More details on each point: ...

