//Copyright 2012 Manning Publications Co.
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.
//
import org.apache.chemistry.opencmis.commons.*
import org.apache.chemistry.opencmis.commons.data.*
import org.apache.chemistry.opencmis.commons.enums.*
import org.apache.chemistry.opencmis.client.api.*

// def cmis = new scripts.CMIS(session)
// println session.repositoryInfo.name
// cmis.printObjectSummary "/"

//<start id="updateProps"/> 
def someDoc = session.getObjectByPath("/my first folder/sample-a.pdf")

println("Before: " + someDoc.name)

def props = ['cmis:name': 'sample-c.pdf']

someDoc.updateProperties(props, true)//<co id="refreshTrue" />

println("After: " + someDoc.name)
//<end id="updateProps"/> 
