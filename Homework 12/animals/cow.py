{"payload":{"allShortcutsEnabled":true,"fileTree":{"lesson_14/animals":{"items":[{"name":"__init__.py","path":"lesson_14/animals/__init__.py","contentType":"file"},{"name":"animal.py","path":"lesson_14/animals/animal.py","contentType":"file"},{"name":"cow.py","path":"lesson_14/animals/cow.py","contentType":"file"},{"name":"dog.py","path":"lesson_14/animals/dog.py","contentType":"file"},{"name":"hen.py","path":"lesson_14/animals/hen.py","contentType":"file"}],"totalCount":5},"lesson_14":{"items":[{"name":"animals","path":"lesson_14/animals","contentType":"directory"},{"name":"animal_farm.py","path":"lesson_14/animal_farm.py","contentType":"file"},{"name":"oop_paradigms.py","path":"lesson_14/oop_paradigms.py","contentType":"file"}],"totalCount":3},"":{"items":[{"name":"lesson_1","path":"lesson_1","contentType":"directory"},{"name":"lesson_10","path":"lesson_10","contentType":"directory"},{"name":"lesson_11","path":"lesson_11","contentType":"directory"},{"name":"lesson_12","path":"lesson_12","contentType":"directory"},{"name":"lesson_13","path":"lesson_13","contentType":"directory"},{"name":"lesson_14","path":"lesson_14","contentType":"directory"},{"name":"lesson_15","path":"lesson_15","contentType":"directory"},{"name":"lesson_16","path":"lesson_16","contentType":"directory"},{"name":"lesson_17","path":"lesson_17","contentType":"directory"},{"name":"lesson_2","path":"lesson_2","contentType":"directory"},{"name":"lesson_4","path":"lesson_4","contentType":"directory"},{"name":"lesson_5","path":"lesson_5","contentType":"directory"},{"name":"lesson_6","path":"lesson_6","contentType":"directory"},{"name":"lesson_7","path":"lesson_7","contentType":"directory"},{"name":"lesson_8","path":"lesson_8","contentType":"directory"},{"name":"lesson_9","path":"lesson_9","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"Git Basic Console Commands.md","path":"Git Basic Console Commands.md","contentType":"file"},{"name":"LICENSE","path":"LICENSE","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"beginner_tasks.md","path":"beginner_tasks.md","contentType":"file"},{"name":"function_tasks.md","path":"function_tasks.md","contentType":"file"},{"name":"list_tasks.md","path":"list_tasks.md","contentType":"file"}],"totalCount":23}},"fileTreeProcessingTime":9.569994999999999,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":636801680,"defaultBranch":"main","name":"learn-python-hillel-05-05-2023","ownerLogin":"kyrrylo","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-05-05T20:18:46.000+03:00","ownerAvatar":"https://avatars.githubusercontent.com/u/60550488?v=4","public":true,"private":false,"isOrgOwned":false},"refInfo":{"name":"main","listCacheKey":"v0:1683307127.0","canEdit":true,"refType":"branch","currentOid":"2f85c8df383548f1e6db5f179248cf2205388824"},"path":"lesson_14/animals/cow.py","currentUser":{"id":131864688,"login":"Denysius","userEmail":"Denis4Broker@gmail.com"},"blob":{"rawLines":["from .animal import Animal","","","class Cow(Animal):","    # init так же называют конструктором класса","    def __init__(self, name: str, age: int, say_word='Мууууууу!'):","        \"\"\"","        Класс отвечает за симуляцию животного коровы","        \"\"\"","        super().__init__(","            name=name,","            age=age,","            say_word=say_word,","            preferred_food={'трава', 'сено'}","        )","        self.animal_type = 'Корова'","","    def treat(self, hours: int) -> str:","        \"\"\"","        Ухаживая за коровой должное количество времени, мы получаем молоко","        :param hours: время ухаживания","        :return: молоко или ничего","        \"\"\"","        if hours > 1:","            print(f'Вы ухаживаете за {self} {hours} часов и получаете ведро молока')","            return 'Ведро молока'","        print(f'Вы ухаживаете за {self} {hours} часов.')","        return ''"],"stylingDirectives":[[{"start":0,"end":4,"cssClass":"pl-k"},{"start":6,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-k"},{"start":20,"end":26,"cssClass":"pl-v"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":9,"cssClass":"pl-v"},{"start":10,"end":16,"cssClass":"pl-v"}],[{"start":4,"end":47,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":29,"end":32,"cssClass":"pl-s1"},{"start":34,"end":37,"cssClass":"pl-s1"},{"start":39,"end":42,"cssClass":"pl-s1"},{"start":44,"end":52,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-c1"},{"start":53,"end":64,"cssClass":"pl-s"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":52,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":16,"end":24,"cssClass":"pl-en"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":16,"end":19,"cssClass":"pl-s1"}],[{"start":12,"end":20,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":21,"end":29,"cssClass":"pl-s1"}],[{"start":12,"end":26,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":35,"cssClass":"pl-s"},{"start":37,"end":43,"cssClass":"pl-s"}],[],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":35,"cssClass":"pl-s"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-s1"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":32,"end":34,"cssClass":"pl-c1"},{"start":35,"end":38,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":74,"cssClass":"pl-s"}],[{"start":0,"end":38,"cssClass":"pl-s"}],[{"start":0,"end":34,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":83,"cssClass":"pl-s"},{"start":37,"end":43,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-kos"},{"start":38,"end":42,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-kos"},{"start":44,"end":51,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-kos"},{"start":45,"end":50,"cssClass":"pl-s1"},{"start":50,"end":51,"cssClass":"pl-kos"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":33,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":55,"cssClass":"pl-s"},{"start":33,"end":39,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-kos"},{"start":34,"end":38,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-kos"},{"start":40,"end":47,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-kos"},{"start":41,"end":46,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-kos"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":17,"cssClass":"pl-s"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/kyrrylo/learn-python-hillel-05-05-2023/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/kyrrylo/learn-python-hillel-05-05-2023/security/dependabot","repoSecurityAndAnalysisPath":"/kyrrylo/learn-python-hillel-05-05-2023/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"cow.py","displayUrl":"https://github.com/kyrrylo/learn-python-hillel-05-05-2023/blob/main/lesson_14/animals/cow.py?raw=true","headerInfo":{"blobSize":"1.09 KB","deleteInfo":{"deletePath":"https://github.com/kyrrylo/learn-python-hillel-05-05-2023/delete/main/lesson_14/animals/cow.py","deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"f022cb0","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fkyrrylo%2Flearn-python-hillel-05-05-2023%2Fblob%2Fmain%2Flesson_14%2Fanimals%2Fcow.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"28","truncatedSloc":"25"},"mode":"file"},"image":false,"isCodeownersFile":null,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","large":false,"loggedIn":true,"newDiscussionPath":"/kyrrylo/learn-python-hillel-05-05-2023/discussions/new","newIssuePath":"/kyrrylo/learn-python-hillel-05-05-2023/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/kyrrylo/learn-python-hillel-05-05-2023/blob/main/lesson_14/animals/cow.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/kyrrylo/learn-python-hillel-05-05-2023/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"kyrrylo","repoName":"learn-python-hillel-05-05-2023","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"Cow","kind":"class","identStart":35,"identEnd":38,"extentStart":29,"extentEnd":1112,"fullyQualifiedName":"Cow","identUtf16":{"start":{"lineNumber":3,"utf16Col":6},"end":{"lineNumber":3,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":3,"utf16Col":0},"end":{"lineNumber":27,"utf16Col":17}}},{"name":"__init__","kind":"function","identStart":136,"identEnd":144,"extentStart":132,"extentEnd":525,"fullyQualifiedName":"Cow.__init__","identUtf16":{"start":{"lineNumber":5,"utf16Col":8},"end":{"lineNumber":5,"utf16Col":16}},"extentUtf16":{"start":{"lineNumber":5,"utf16Col":4},"end":{"lineNumber":15,"utf16Col":35}}},{"name":"treat","kind":"function","identStart":535,"identEnd":540,"extentStart":531,"extentEnd":1112,"fullyQualifiedName":"Cow.treat","identUtf16":{"start":{"lineNumber":17,"utf16Col":8},"end":{"lineNumber":17,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":17,"utf16Col":4},"end":{"lineNumber":27,"utf16Col":17}}}]}},"copilotUserAccess":{"canModifyCopilotSettings":false,"canViewCopilotSettings":false,"accessAllowed":false,"hasCFIAccess":true,"hasSubscriptionEnded":false,"business":null},"csrf_tokens":{"/kyrrylo/learn-python-hillel-05-05-2023/branches":{"post":"dLkplzdVzd8s9tKDnSSYTKcFWpCWnUTZnHGsdWeKkPLtyutIMv3TA9eMIa1hjncmp_WVtG7Kc6pvF5j8gZPMfQ"}}},"title":"learn-python-hillel-05-05-2023/lesson_14/animals/cow.py at main · kyrrylo/learn-python-hillel-05-05-2023","locale":"en"}