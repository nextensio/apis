/*
 * Controller APIs
 *
 * APIs to act on Nextensio Controller
 *
 * API version: 1.0.0
 * Contact: development@nextensio.com
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type Tenant struct {
	Result string `json:"Result"`
	Id string `json:"_id"`
	Name string `json:"name"`
	Group string `json:"group"`
	Domains []string `json:"domains"`
	Easymode bool `json:"easymode"`
	Splittunnel bool `json:"splittunnel"`
	Cfgvn string `json:"cfgvn"`
	Idps []string `json:"idps"`
	Admgroups []string `json:"admgroups"`
	Type_ string `json:"type"`
	Mspid string `json:"mspid"`
	Mgdtenants []string `json:"mgdtenants"`
}