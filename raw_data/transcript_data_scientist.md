**Transcript with Jimmy, Data Scientist**

January 24, 2025, 9:33PM

**John** started transcription

**John**   0:03  
 Go like that.  
 So sorry, you'll have to opt back in.  
 So.  
 So yeah, is that your understanding of what data can store is or did you have a different idea?

**Jimmy**   0:14  
 Yeah.  
 That's pretty much it.

**John**   0:17  
 OK, OK, cool.  
 You know, so let's start off with this just for my understanding.  
 What are the primary responsibilities that you have?

**Jimmy**   0:28  
 So I leave the it's called the computer vision team.  
 Just for lack of a better term.

**John**   0:35  
 OK.

**Jimmy**   0:35  
 So we do imagery and kind of advanced models like that.

**John**   0:43  
 Oh.

**Jimmy**   0:47  
 Yeah. So I have a team, we have different projects.  
 We work on.  
 Like satellite data, we have a phone scanning thing.  
 We provide work.  
 Flow optimization models basically.  
 I don't know if any of that makes any sense, but that's kinda OK.

**John**   1:10  
 It does.  
 Yeah, I I know.  
 Appraiser product that she they go out and they take.  
 Sorry, there's an animal I've not seen before in my yard.  
 So like what?  
 What is that?  
 I think it's a mole.  
 I hope it's a Moll.

**Jimmy**   1:30  
 Oh.  
 OK.

**John**   1:32  
 Yeah. Anyway, yeah, I I I know if appraisal product, they go out and they take photos and then analyze.  
 To help them with their workflow. So things like that kinda more or less. OK. Sala mode, yeah.

**Jimmy**   1:43  
 OK.  
 Yeah. So the the Ala mode, yeah. And further into the further into the guts as well, yeah.

**John**   1:52  
 OK, OK, cool. Great, great.  
 Hey, Pablo, he's our TPM for this initiative.  
 So he's joining to help us with, you know, here in first hand.

**Jimmy**   2:03  
 Yeah.

**John**   2:05  
 So let's let's hear first hand. So when?  
 You're when you're working through the data catalog or our assets. What what challenges do you and your team face?  
 Trying to find information.  
 I I know it's a lot.

**Jimmy**   2:24  
 Yeah.

**John**   2:24  
 I I just what comes up?  
 What? What's what's first?

**Jimmy**   2:27  
 How do we do it?

**John**   2:29  
 Yeah, we can start with the workflow, yeah.

**Jimmy**   2:30  
 Or.  
 So what we usually do is.  
 A mix of.  
 Tribal knowledge from me.  
 There are a few key people we can ask that understand what's going on in the data.  
 And then there's usually a product component, right?  
 And we'll just go off into the ether.  
 And decide what to do.  
 Typically there's, you know, some kind of product involvement and it's typically an existing.  
 Product and so that data is almost always required to satisfy their needs.  
 So those are kind of the three ways we.

**John**   3:15  
 OK.

**Jimmy**   3:21  
 Right, figure out what data is out there.

**John**   3:27  
 Do that.  
 How do you figure that out?

**Jimmy**   3:31  
 So for.  
 Tribal knowledge. It's been I've been here for eight 8-9 years, something like that and so.  
 There was most of the stuff that's in SDAP now that we can access used to be in something called one source.

**John**   3:52  
 I don't think I know that one.

**Jimmy**   3:53  
 You probably it's, it's.  
 I mean, it's long gone, but right?

**John**   3:57  
 OK.

**Jimmy**   3:58  
 But it was a short list of all the things.  
 It was a data candy store. So right you got access to the SQL Server and it was like these are all the data sets that the data scientists might be interested in.

**John**   4:04  
 OK.

**Jimmy**   4:12  
 And so they dumped it all there.

**John**   4:12  
 OK.

**Jimmy**   4:14  
 And you could just go look through it, right?  
 And it was documented.  
 And then when they moved it to.

**John**   4:18  
 OK.

**Jimmy**   4:21  
 Google cloud.  
 How all that went away and we no longer had a centralized system anymore.

**John**   4:28  
 What do you have to do now?

**Jimmy**   4:31  
 So yeah, so it depends.  
 So for product data.  
 Yeah. So we, there's, there's, there's there's kind of two pieces.  
 So yeah. So we'll go ask somebody if it's like, hey, I really want permit data that used to live somewhere.  
 I have no idea where it lives now, so we just go ask people.  
 Occasionally we'll try to do searches in calibra it becomes.  
 Not right.  
 It's it's just not feasible.  
 There's it's too hard to get through that after the, you know, the 30th page.

**John**   5:04  
 OK.

**Jimmy**   5:07  
 Useless results.

**John**   5:08  
 Oh, because of so many results, OK.

**Jimmy**   5:10  
 Either you get no results or you get too many results.

**John**   5:15  
 Yeah.

**Jimmy**   5:15  
 So unless you know exactly what you're looking for.  
 No, it's not gonna work, right. If you know the magic wording that's used to get exactly to what you want.

**John**   5:21  
 OK.  
 Uh huh.

**Jimmy**   5:28  
 So that's where you land. And even if you get to calibra and you find the page, unless you know what you're looking at, it's usually not helpful.  
 So last week.  
 We had the name of the table.  
 We knew exactly what data we were looking at.  
 It was the the text data. I forget what they call it now.  
 It used to be Diablo.  
 One of the guys on my team, he's like I have no idea what these columns mean.  
 That data was unavailable in any place I could find in Calibra, right?

**John**   5:58  
 Oh boy.

**Jimmy**   5:59  
 Like what's in there?  
 So we went to OneDrive and we typed in some column names and we searched until we found some documentation from 2017\.

**John**   6:00  
 OK.

**Jimmy**   6:08  
 And network data dictionary. There we go.

**John**   6:13  
 Wow, that's archaeology, I guess.

**Jimmy**   6:17  
 Spelunking is the term I like to use for for data at core logic, we go data spelunkin a lot.

**John**   6:24  
 OK, OK.  
 Wow.  
 I I hear it's hard to find things, but that is interesting.

**Jimmy**   6:30  
 Yeah.

**John**   6:33  
 That that's a new one for me.

**Jimmy**   6:33  
 Yep, that was, yeah.  
 I no, I yeah, we've, I've not been terribly successful with with kleibra.  
 I.  
 I mean, I don't think it's an open. So I don't think it's a hidden secret.  
 I I've literally told Adam. I've told Adam that.

**John**   6:45  
 No, no, no.  
 Yeah.

**Jimmy**   6:49  
 To his face multiple times.  
 So that's yeah, it is what it is, it's fine.

**John**   6:50  
 Yeah, yeah.  
 OK.

**Jimmy**   6:55  
 So that's, that's where we're at.  
 So the other thing that we do is right, like we go talk to the product.  
 So there's right, insurance is the worst. We work with insurance a lot.  
 None of that stuff gets drug into SDAP for multiple reasons that don't you don't really want to know about.  
 Right starting and ending with money, basically.  
 So it costs lots of money, so because they have a ton of data, it's in different places anyway.  
 So there's also that data. We'll go look through that data. We have a lot of the same challenges, right.  
 So you got to go find somebody that knows what the heck is in this data.  
 Half the time, there's literally nobody that actually understands what's in the data.  
 Or what the different fields are?  
 Right. It's just like, well, I don't know.

**John**   7:39  
 Yeah.

**Jimmy**   7:39  
 And people just fill out whatever they want because they have a way that they use the tools and that's how they use the tools.  
 So there you go.

**John**   7:49  
 Oh boy. So half the time. You know who to talk to.  
 Is that easy to find?

**Jimmy**   7:56  
 For product stuff.

**John**   7:56  
 Who to talk to? Yeah.

**Jimmy**   7:59  
 It's usually right.  
 It's not fun, but it's usually a chain of of you know, OK.  
 Let's start with a product guy, all right.  
 When they get bumped over to the technical and they'll get bumped down the tree until you find somebody that knows about that specific thing.

**John**   8:14  
 OK.  
 Yeah, that. That's what I'm hearing.  
 And when it's not there, you're hoping for a data dictionary.

**Jimmy**   8:17  
 Yeah.

**John**   8:24  
 Digging into archives.

**Jimmy**   8:24  
 So.  
 Yeah. So we'll pull data dictionaries.  
 Those those are not panacea either.  
 But yeah, I sorry I should let you continue on.  
 I don't know what you want to.

**John**   8:40  
 No, I actually this is an interview of you. So I wanna hear those those those problems.

**Jimmy**   8:43  
 OK.

**John**   8:45  
 Yeah. What else is a challenge for you when trying to figure this stuff out?

**Jimmy**   8:51  
 So the data sets OK.  
 So it's kind of related.  
 So people fill out whatever they want, and most of these data sets.  
 And it it always varies as to why they filled out certain things.  
 And you get all kinds of weirdo weirdo stuff.

**John**   9:16  
 Do you mean the descriptions?

**Jimmy**   9:16  
 Right.

**John**   9:19  
 Or what do you mean?

**Jimmy**   9:21  
 So.  
 Yeah. So if you have like a text comment field.  
 Man who knows, right?  
 There's maybe a standard for an appraisal, maybe not.  
 The people that, yes, let's stick with.  
 I spent a lot of time with appraisal data like the original FNC.  
 They call them envs because so that's another common thing, especially for us, is in order to get the images, you had to go get this custom file format.  
 And pull it out right and then it was attached to an XML file that you had to join back across. All of that information.  
 Obviously the the photos aren't loaded into, you know big query, but everything else that goes in there like it's just a lot of that information, is destroyed.  
 As it gets processed out of the XML.

**John**   10:16  
 Oh oh.

**Jimmy**   10:17  
 Right. Because like I, there's there's a bunch of different schemas, right?  
 'Cause people have different things and you can do horrible nested things in XML that do not translate well into your standardized SQL schema.  
 And that's just life, right?  
 It's just life, so.

**John**   10:37  
 Right, right, right.

**Jimmy**   10:41  
 We just dumped the entire XML.  
 Jason for big query reasons into a table and that's what we do when we process it internally on my team 'cause we just said we can't work with what's in SDAP. So we just go get the data right in the format that works for us and and D.  
 It in the right places and then you've got other weirdo things.  
 So there's different conventions.  
 And sometimes, depending on right how the stuff is processed, the original data gets destroyed or gets mapped in certain ways that don't make sense.  
 So like single pin double pin windows is called out. In some appraisals it's a free form text field and there's 137 ways that people have filled that field out at least 1000 times, right?

**John**   11:30  
 OK, OK.

**Jimmy**   11:30  
 So there's a hundred 'cause. It's a free form text field and you literally have thousands of people.  
 That just type in whatever they want, so being able to go back and decode that right. And of course if you try to map it to a core logic.

**John**   11:37  
 Yeah, yeah.

**Jimmy**   11:44  
 You know one in 10 fields like it doesn't.  
 It just doesn't work.  
 So that happens frequently.  
 Occasionally there's I haven't been able to validate this, but one of the former FNC execs told me that you know, you go in, you look on an appraisal, there's check boxes, there's four check boxes for foundation types, I think.  
 No, it's three. So you get a slab, you get a crawl space and you get a basement, so.

**John**   12:12  
 OK.

**Jimmy**   12:13  
 One of the things that's really important for us.  
 Is, you know, houses on the coast, they're up on. I called upon stilts, rather pile. Pier piles are Piers.  
 They're like 20 feet off the ground, 15 feet off the ground.

**John**   12:23  
 Speaker.

**Jimmy**   12:26  
 It's not a crawl space.  
 So, right.  
 And then people will do weird stuff, like they'll actually build underneath it.  
 They're not supposed to the the like, finish the rooms, right?  
 So then, if you're in Hawaii, apparently everybody in Hawaii likes to call those basements.  
 I fear an appraiser.  
 It's a basement at all.  
 Right. So that kind of stuff like people just pick whatever the heck they feel like, so right.

**John**   12:50  
 OK.  
 Yeah, yeah.

**Jimmy**   12:55  
 And then, yeah, and then you get into some of like the tax data, a lot of times, right?  
 And so yeah, every time you have people that have accumulated data into a central location, you've got all the right 'cause the US is the US.  
 Every state, every county has their own way of doing things. Sometimes every person.

**John**   13:13  
 Mm hmm.

**Jimmy**   13:14  
 So you have all these different standards and it's just munged down into.  
 Whatever the guy doing it right.  
 Like whatever his use case was, which may not have been anything more than put all this these fields into one place.  
 And so then you've got to go back and figure out, well, OK, like half this data is just like it just it's garbage.  
 It doesn't make sense.  
 So then you have to go back to the original data and figure out kind of OK like what was actually in there and try to decipher the the madness that.  
 Happened to get to kind of the.  
 The the data state that it is.

**John**   13:51  
 So every time you take on.  
 A work item.  
 You're starting from scratch, basically.  
 You're looking at the raw data, figuring it out.

**Jimmy**   14:04  
 As yes or no. So right? So have I looked through all 240 columns in the MLS data that's in SDAP multiple times.  
 Yes, I've plotted those on multiple times.  
 Will you ever get away from that?  
 No. If you want to date a candy store, do you guys need to duplicate that?  
 Yes, if the data scientists are gonna use it, that's like there's no there's no escaping from that.

**John**   14:26  
 Mm hmm.

**Jimmy**   14:30  
 That is, that's part of what you have to do, right?

**John**   14:30  
 Mm hmm.

**Jimmy**   14:33  
 So your statistician 101, the first thing you do is plot the data, generate summary statistics, and you look at it.  
 So that's that, that part.  
 Like I don't ever have to go back and relook at number of stories in square footage. And you're built because I've done it enough.  
 I know what's going to be in there now if I pull a new data set.

**John**   14:53  
 Mm hmm.

**Jimmy**   14:54  
 Yeah, I look at it again, but right, like I like, I know what to expect.

**John**   14:58  
 I see.  
 I see.

**Jimmy**   15:02  
 So that.

**John**   15:02  
 So.

**Jimmy**   15:03  
 That moves the needle a little bit.

**John**   15:05  
 OK, so as you accumulate this knowledge that's in your head, then it's easier over time. Your experience with the with the data, the nature of it.  
 So a new data scientist coming onto the team, they're gonna really struggle, I assume.  
 How could we help them with interpreting finding this information?

**Jimmy**   15:32  
 So there's there's different ways that people approach.  
 Models so we don't always do a great job at like you.  
 You have.  
 You have to plot the data that frequently does not happen.  
 One, it takes a lot of time to look through it.  
 Two, it's kind of a pain in the rear to plot it so right.  
 Like I basically found indoor build tools to do that so that you could push the button and it generated it all 230\.  
 Instead of having to type it up 230 times 'cause that that's not gonna fly.

**John**   16:06  
 Nice, nice.

**Jimmy**   16:08  
 It's not gonna fly.

**John**   16:09  
 Yes, yes.

**Jimmy**   16:11  
 So automatically generating those that's, that's where we wanna be. So calibra I think might have some of that built in and it's all disabled because you're not allowed to look at the Tate until you get permission.

**John**   16:24  
 I don't know about that, yeah.

**Jimmy**   16:24  
 So they'll they'll they'll calculate fill rates and you're like, that's nice. Like, that's one out of about 3 things you need to look at and it may or may not even be the most useful, depending on what you're doing.

**John**   16:38  
 What are those other two things that are important for you to look at?

**Jimmy**   16:42  
 So it depends on whether it's numeric or categorical or string.  
 If it's string, your life kind of sucks.  
 If it's, if it's truly like a small number of categories, you look at the distribution, right?  
 So counts percentages, whatever. If it's numeric you want to plot it on a graph, and it depends on what kind of number in the distribution to see.

**John**   16:59  
 OK.

**Jimmy**   17:07  
 Sometimes there's some things you need to do to make it actually visualizable.

**John**   17:13  
 OK.

**Jimmy**   17:13  
 So oh, you're you're built as a fun one if you plot raw, you're built out of any data set in SDAP, and you let it auto do it. You'll see a small bump at the year 0\.  
 And you'll see one bar around the year 2000, because that's life, right?  
 Oh, and you'll see another small bar at the year 3000\.

**John**   17:37  
 This is what someone entered just those outliers that really mess up.

**Jimmy**   17:40  
 Somebody, somebody put it in?  
 And so you right.  
 So there's wet, like there's easy, like standardized ways to deal with that kind of garbage.  
 You just.  
 You just flip that switch and then OK.  
 Yeah, here we go.

**John**   17:53  
 OK, OK.

**Jimmy**   17:54  
 You can't always do it so, but there's there's fairly automated ways to do most of this.

**John**   17:56  
 Hey Cortana.  
 OK.  
 But string, you just have to read it all.  
 Or do you just take a sample set?

**Jimmy**   18:04  
 I I it depends on what it is.  
 So if it's category categorical ish so right, so there there's certain things they're supposed to do. We'll still do.  
 We'll still build a distribution, right and OK, fine.  
 There's there's 20,000 different things, but there's actually a lot of repeats.  
 So then you got to go in and fix, you know.

**John**   18:27  
 OK.

**Jimmy**   18:30  
 You can start combining some of them.  
 And there's probably ways to automate some of that, and then you have other things where it's like MLS description and you just have to go read some random ones like there's not really a better way to do that.

**John**   18:45  
 OK, OK.

**Jimmy**   18:45  
 So you can generate like how long are they type statement.  
 But I mean, it's just it's an MLS description.  
 So.

**John**   18:55  
 Yeah. Yeah, those are, yeah, basically marketing speak.

**Jimmy**   18:56  
 Yeah.  
 Yeah. So yeah, so right.

**John**   18:59  
 Yeah, I've heard enough.

**Jimmy**   19:01  
 Yeah. Then your your toolbox becomes pretty large in terms of the things you can do to analyze those. It's not.  
 It's not easily automated I guess is really what I would say.  
 Gotta pick the three.

**John**   19:12  
 I.  
 I I get that.

**Jimmy**   19:13  
 Yeah. So yeah, you get 20 things instead of three.

**John**   19:14  
 OK.  
 OK.  
 Do you?  
 Can we talk about data lineage?  
 Is that something that comes into play where it's coming from?

**Jimmy**   19:27  
 Oh yeah.

**John**   19:27  
 How it transforms where it goes?

**Jimmy**   19:32  
 Yeah. So you probably figured out. I like to go back to the original source where possible.  
 If I get transformed data, we usually spend a fair amount of time trying to understand and map that back to maybe what it actually was. And so for a lot of the work we do, it's actually a lot more straightforward than what you probably find with others because.

**John**   19:53  
 MMM.

**Jimmy**   19:59  
 Most of the time we'll pull up photos.  
 So that makes a huge difference.  
 Makes a huge difference if you can see the house where you can see right around the house.  
 In terms of being able to figure some of these things out 'cause you you know you plot 10 photos of.  
 You know a crawl space. You start to see a pattern even if you don't know what a crawl space is.  
 You can, right, you can start to try to figure it out.

**John**   20:25  
 Hmm.

**Jimmy**   20:28  
 So that's that's one of the big things.  
 And I'm completely lost.  
 What are we?  
 What are we talking about?

**John**   20:33  
 Oh, we'll start lineage, basically.

**Jimmy**   20:36  
 Oh yeah. So yeah. And then, yes, before we start building models with anything.  
 We've usually, even if it's in calibra, we've usually gone and asked somebody.  
 So I think Indira is trying to change the process which is good 'cause the previous process was I literally just emailed Mark and Yianni.

**John**   20:59  
 Yeah, I need to. OK, sure.

**Jimmy**   21:00  
 Yes, Mark andorianni. Yeah, I know.

**John**   21:02  
 OK.

**Jimmy**   21:03  
 I yeah, I I have AI have a close relationship with Yianni.  
 I ask him a lot of hard questions.

**John**   21:09  
 Oh wow. I I didn't know he would be a resource for this.

**Jimmy**   21:13  
 I don't know that he really wants to be a resource, but he's a nice guy and the answers by emails.  
 So he is.

**John**   21:20  
 So kind.  
 That's so great. That's great. OK, alright.

**Jimmy**   21:26  
 Yeah. Yeah, because yeah, because there's there's different.

**John**   21:27  
 Cool.  
 Yeah, go ahead.

**Jimmy**   21:32  
 There's a lot more basically for the imagery stuff, a lot of times we can build on one data set and then deploy it on other data sets.  
 It's a lot harder in the tabular world, right?  
 But I can train stuff on appraisal and use it on MLS, or I can train stuff on MLS and use it in appraisal.

**John**   21:49  
 Mm hmm.

**Jimmy**   21:50  
 Which is actually more common.  
 Right 'cause. There's different restrictions around what you can and can't do.  
 With that data.  
 And so that's, that's where we land in terms of, right?  
 So we have a very distinct training versus like production deployment.  
 Everything, so everything is completely different, completely separate.  
 So the training stuff is completely distinct.  
 There's a lot of data that goes into training we never touch in production at all, ever.

**John**   22:23  
 OK.

**Jimmy**   22:24  
 So yeah, so we.  
 We pay close attention to that and I understand all the as much as we can, all the gotchas before we start and then we go through the MRC to make sure we didn't do anything dumb.  
 Right.

**John**   22:36  
 OK.  
 I'm sorry, MRC.

**Jimmy**   22:39  
 Model review committee.  
 So that's like the final step.

**John**   22:41  
 Oh, oh, yes.

**Jimmy**   22:43  
 There's a legal and compliance and all kinds of checks, but yeah, one of the big things they do is look through all the data.  
 What data did she use?  
 Where did you use it? How's it?  
 Where where's it gone?  
 Is that approved, etcetera, etcetera.

**John**   22:57  
 OK, OK.  
 You you touched on fill rates earlier?  
 That was sort of useful, but you're saying not doesn't tell you the whole picture. Is that what I understood?

**Jimmy**   23:13  
 Yeah, that doesn't.  
 That does not even come close.  
 Yeah, right.  
 So if I tell you we have, you know, 9090% coverage on your built and half of EM are zero, that doesn't really help you.

**John**   23:26  
 Right. OK. OK.

**Jimmy**   23:28  
 Quite as much as that initial number might indicate, right? So.

**John**   23:33  
 OK.

**Jimmy**   23:33  
 Yeah.

**John**   23:33  
 So it's really about building those stats, looking at the sample data, so really understand it, OK.

**Jimmy**   23:37  
 Yes. Yep. Yeah, I I understand.  
 Yeah. Fill rates are a big deal, but it's not the whole story.

**John**   23:46  
 Project managers really like fill rates, but it's different for for data scientists. It's interesting.

**Jimmy**   23:50  
 They do.  
 No, it's it's not.  
 They just they're they're not paying attention, right.  
 Or they don't care.  
 Because.

**John**   24:03  
 You know, and that's totally valid, yeah.

**Jimmy**   24:04  
 Their customers, they're. I guarantee you their customers. They're either not using the data or they know it's wrong and they're mad at us.  
 Like would you?  
 Why would you like? Why would you pay for your bill where half of them are 0?  
 You can't call that filled.

**John**   24:17  
 Right.

**Jimmy**   24:18  
 That's that's ridiculous.

**John**   24:20  
 Right, right. Interesting.

**Jimmy**   24:26  
 Yeah.

**John**   24:28  
 OK.  
 That's interesting.  
 All right.  
 Well, that's that's really something for the team to to talk about.  
 Indira is on our team, so she's we're working together to come up with this with a solution. What? That's great.

**Jimmy**   24:34  
 Yeah. OK.

**John**   24:43  
 So.  
 I was talking with Amy the other day and.  
 She filled me in that you guys help with.  
 Cost estimates for using this these data sets is that so?  
 Did I understand that correctly?

**Jimmy**   25:05  
 What do you mean?

**John**   25:07  
 She was saying that data scientists help with.  
 Gosh.  
 They report back the.  
 Estimates of what would cost to get or to to use this data and a product.  
 And helps with formulating.  
 Some sort of ROROI on creating this new solution?  
 But maybe that's not how I understood it then.

**Jimmy**   25:34  
 So. So there's a couple different ways it could be.  
 So there's like for MLS data, there are royalties.  
 So right, if you got to pay $10 million and it provides barely anything in terms of improvement, you'll pay the ten $10 million and drop it, right?

**John**   25:57  
 Right, right.

**Jimmy**   25:59  
 I guess there are probably also costs in terms of, Oh yeah, it's gonna cost an extra 50 grand in.  
 Development time to bring in that data set.  
 That would be a little the same.

**John**   26:12  
 OK.

**Jimmy**   26:13  
 I could think of that might match.  
 I don't know what your after.

**John**   26:15  
 That might have.  
 That might have been what she was referring to.

**Jimmy**   26:18  
 OK.

**John**   26:19  
 So for let's say the royalties, how do you determine that?

**Jimmy**   26:26  
 For the royalties, so you should be calculating some kind of statistics, right? So.  
 Model or not you you go look at you know accuracy and valid coverage, right?  
 So those are two things.  
 How accurate is this and what's? What's the coverage?

**John**   26:40  
 OK.  
 OK.

**Jimmy**   26:46  
 Basically so and then you can compare oh with it. You know, we're at 90% without it.  
 We're at 20%.  
 It's a huge deal versus, you know, 89 and 90\.  
 It's not really that.  
 Not big a deal.

**John**   26:58  
 OK, OK.  
 So.  
 Hypothetically, if you were to log into cloud desktop later this year and you saw a new tool that.  
 Isn't Calibra, but works with calibra.  
 And it's going to help you and your team with with.  
 Making it easier to find this information, get you to the answer faster.  
 What would you hope to see in that?

**Jimmy**   27:37  
 So for us, for me, for me personally, the the primary thing is going to be understanding what is available.

**John**   27:51  
 OK.

**Jimmy**   27:51  
 For different categories of data.  
 So there's data about people I do not touch that don't want to look at it.  
 There's data about properties.  
 Right, which can be split into parcels or structures. So right and there's data that doesn't fall into any of those.  
 There's maybe utilities data.  
 Right. That our Geo that's better.  
 So there's you.  
 Well, geospatial data, right?  
 That describes I don't lakes or.  
 Yeah. OK.  
 That's it's like pipes running through the utilities, right?  
 That's not a partial specific thing.

**John**   28:29  
 OK.

**Jimmy**   28:30  
 So how do we get those different categories? And then we wanna be able to.

**John**   28:34  
 Mm hmm.

**Jimmy**   28:36  
 Understand the.  
 The the use rights and so.

**John**   28:43  
 Yes.

**Jimmy**   28:46  
 For for us it seems like there really is.  
 Like, there's only a few different types.  
 Like I get.  
 There's only a few different types of contracts that really seem to get written right, and it's like you can use it here. You can use it there, you can't use it here. You can't use it there. And then there's royalties or not royalties. And then then these are.  
 The only business units that are allowed to use it, so that to me looks like.  
 And this is going back.  
 You're like it.  
 It kind of feels like, well, why can't you just do like?  
 You know, like a government, you know, classified super top secret or regular type, right?  
 You just you just throw classifications on it for a quick, you know, quick look through.  
 To whatever and then.  
 That's so that's a big one. And then the the last piece is.  
 Once we have all of this kind of sorted out right, so it's like, OK, well, I wanna know about properties.  
 I wanna know everything we have to.  
 To know about your belt.  
 I think there are like three or four different ways that people literally write out your built.  
 You can't just go type in your built. You have to look at all the columns.  
 'Cause, that's just life, right?

**John**   30:03  
 Yeah.

**Jimmy**   30:03  
 And then.  
 So that's that's for target.  
 So I know I want this thing if I'm trying to predict your build, there are a lot of things that impact that that I don't understand and I will probably never understand.  
 In in the promise of machine learning as opposed to.

**John**   30:20  
 Hmm.

**Jimmy**   30:26  
 1920s statistical models is that I can take all 10,000 columns that may or may not be useful to me and shove them into my model and my model will tell me what's useful.

**John**   30:40  
 Interesting.

**Jimmy**   30:40  
 So if I have to go ask for each one of those 10,000 columns, we will always be behind, right?  
 We're not gonna do that.

**John**   30:48  
 OK. Right. Right. Yeah.

**Jimmy**   30:51  
 And that leads me back to the yeah. What? What can I?

**John**   30:53  
 Cool.

**Jimmy**   30:54  
 What can I just pull down and use?  
 And it right?  
 Well, once I find the value then I can go figure out if it's worth it. But like to be able to just check off large swaths in somewhat automated fashion without having to go through and ask for permission for each column.

**John**   31:06  
 Yeah.  
 Yeah.

**Jimmy**   31:13  
 Specifically beforehand.

**John**   31:14  
 OK. OK. OK.  
 I I hope that's something we can get you OK.

**Jimmy**   31:17  
 Yeah.  
 It's yeah.

**John**   31:24  
 Permissible use. How do you get that now?  
 What's that like?

**Jimmy**   31:27  
 So if I know where it is, it's in calibra, right?  
 What it is, and I kinda have these categorizations.

**John**   31:34  
 Mm hmm.

**Jimmy**   31:35  
 Like I said, my brain where it's like it's a do whatever you want. It's a you can only use it for these business products.  
 You can use it for training.  
 You can use it for inference. So the first time we hit one we have, we go to Mark or I guess into your now and figure it out every time after that right?  
 Myself or somebody else on the team knows is like, oh, yeah, you can do blah blah blah.  
 And then we'll get it validated at the end when we go to the MRC thing.

**John**   32:06  
 OK.  
 So travel knowledge basically for the most part.

**Jimmy**   32:08  
 Yep.  
 Yep.

**John**   32:10  
 That's what everyone is saying, OK?

**Jimmy**   32:13  
 Yes, that. That's. Yeah, it's. Yeah, it's too hard.

**John**   32:18  
 Yeah, yeah.

**Jimmy**   32:18  
 Defined in calibra, yeah.

**John**   32:21  
 OK.  
 Well, this has been really great.  
 You've you've really uncovered and validated a lot of the problems that we're hearing and and giving us some great insights.  
 Is there anything that I haven't mentioned? You might want to share? I don't know.  
 Something important as we work through a solution.

**Jimmy**   32:44  
 Oh.  
 I'm not sure.  
 Well, I don't know.  
 I can tell you my my opinions.  
 I'm not sure that the pass forward is to get literally every single column of data across all products into said data Candy store.

**John**   33:21  
 OK.

**Jimmy**   33:21  
 Or any anything that's broadly accessible.

**John**   33:24  
 OK.

**Jimmy**   33:26  
 I don't think that's wise.

**John**   33:29  
 Yeah, that might be too much.

**Jimmy**   33:30  
 For multiple reasons.

**John**   33:33  
 Is there a group that you think we should take priority over?

**Jimmy**   33:33  
 Yeah.  
 I I'm just thinking through different kind of products.  
 It's not like a lot of the stuff that's in sdip.  
 It's like it's the stuff that's always been there.  
 It's not necessarily the things that are are are useful broadly.  
 So that's one one piece.  
 We've talked about a lot of things, the imagery stuff. Everybody always wants to try to grab it and put it in and then they realize that it's like 100 terabytes or something and then they're like, well, maybe we don't want to do that.  
 And I don't.  
 I.  
 I don't know how to solve that one 'cause it should be a lot more useful for people, but it it's not.  
 And then.  
 Modeled outputs. I don't know if that's a thing you guys are looking at as well.  
 So there's raw data.

**John**   34:34  
 Sure.

**Jimmy**   34:36  
 And then there's modeled write data.  
 So if everybody else on your block has an asphalt shingle roof and we don't know what yours is, chances are it's an asphalt shingle roof.  
 That's a model, right?

**John**   34:50  
 Mm hmm.

**Jimmy**   34:52  
 So that is potentially useful information.  
 There's I'm not aware of it. Anyway to go grab that at all right now?

**John**   35:00  
 Yeah, I don't think we've talked about model data output.  
 That's interesting.  
 OK, cool.

**Jimmy**   35:09  
 'Cause it.  
 Is it is distinct from the original data source and has its own set of issues.

**John**   35:15  
 Yeah, yeah, I I can see that.  
 Alright, alright.  
 That's something for the team to figure out if it's gonna be in scope or not.  
 I.  
 I.  
 I don't know.  
 I don't.

**Jimmy**   35:25  
 There you go.

**John**   35:28  
 OK.  
 Well, hey, this has been great.  
 I really appreciate you taking the time. And yeah, as we progress and and work on, you know, deciding if we're gonna build a solution and and start to create waterframes prototypes for possible solution.  
 I'd love to reach out to you and, you know, put you in front of it and say, hey, is this gonna help or not?  
 If we can get there, let her know.

**Jimmy**   35:53  
 OK.

**John**   35:54  
 But, but yeah, yeah, yeah, I'll, I'll, I'll let you go.  
 But thanks so much so much and it's nice meeting you.

**Jimmy**   36:01  
 Yeah. It's nice to meet you.

**John**   36:03  
 OK, take care.

**Jimmy**   36:04  
 Thanks you too. Bye.

**John** stopped transcription

