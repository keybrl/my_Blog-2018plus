# HTTP/1.1 - 状态码定义

> 对 Hypertext Transfer Protocol -- HTTP/1.1 中关于状态码定义的翻译
>
> date: 2017-12-19

---

> part of [Hypertext Transfer Protocol -- HTTP/1.1](https://www.w3.org/Protocols/rfc2616/rfc2616.html)  
> RFC 2616 Fielding, et al.

这篇文章是 *[Hypertext Transfer Protocol -- HTTP/1.1](https://www.w3.org/Protocols/rfc2616/rfc2616.html)* 的一部分  
*RFC 2616* ，Fielding等人所著

## 10 Status Code Definitions （状态码定义）

> Each Status-Code is described below, including a description of which method(s) it can follow and any metainformation required in the response.

下面是对于每个状态码的描述，包括它们适用的请求方法和响应中所需附带的信息。

### 10.1 Informational 1xx （提示信息）

> This class of status code indicates a provisional response, consisting only of the Status-Line and optional headers, and is terminated by an empty line. There are no required headers for this class of status code. Since HTTP/1.0 did not define any 1xx status codes, servers MUST NOT send a 1xx response to an HTTP/1.0 client except under experimental conditions.

这类状态码表示临时响应，响应仅包含状态行、可选的响应头部和作为响应结束标志的空行。这类状态码没有必需附带的响应头部。由于HTTP/1.0没有定义任何1xx状态码，因此服务器 **绝不能** 向HTTP/1.0客户端发送1xx响应，除非是作为实验而进行。

> A client MUST be prepared to accept one or more 1xx status responses prior to a regular response, even if the client does not expect a 100 (Continue) status message. Unexpected 1xx status responses MAY be ignored by a user agent.

在等待接收一个一般（regular）的响应时，客户端 **必须** 准备好接收一个或多个1xx状态的响应，即使客户端并不期望接收一个 `100 (Continue)` 状态的消息。未预料的1xx状态的响应 **可能** 会被用户代理（user agent）忽略。

> Proxies MUST forward 1xx responses, unless the connection between the proxy and its client has been closed, or unless the proxy itself requested the generation of the 1xx response. (For example, if a
>
> proxy adds a "Expect: 100-continue" field when it forwards a request, then it need not forward the corresponding 100 (Continue) response(s).)

代理（proxy） **必须** 转发1xx响应，除非代理和客户端之间的连接已经关闭，或者除非代理本身要求产生1xx响应。（例如，如果代理在转发请求时添加了 `Expect：100-continue` 字段，则它不需要转发相应的 `100 (Continue)` 响应。）

#### 10.1.1 100 Continue （继续）

> The client SHOULD continue with its request. This interim response is used to inform the client that the initial part of the request has been received and has not yet been rejected by the server. The client SHOULD continue by sending the remainder of the request or, if the request has already been completed, ignore this response. The server MUST send a final response after the request has been completed. See section [8.2.3](https://www.w3.org/Protocols/rfc2616/rfc2616-sec8.html#sec8.2.3) for detailed discussion of the use and handling of this status code.

客户端 **应该** 维持其请求。此临时响应用于通知客户端，请求的初始部分已被接收并且未被服务器拒绝。客户端 **应该** 继续发送请求的其余部分，如果请求已经完成，则忽略这个响应。请求完成后，服务器 **必须** 发送最终响应。关于该状态码的使用和处理的详细讨论见[8.2.3](https://www.w3.org/Protocols/rfc2616/rfc2616-sec8.html#sec8.2.3)节。

#### 10.1.2 101 Switching Protocols （切换协议）

> The server understands and is willing to comply with the client's request, via the Upgrade message header field (section 14.42), for a change in the application protocol being used on this connection. The server will switch protocols to those defined by the response's Upgrade header field immediately after the empty line which terminates the 101 response.

服务器理解并愿意依照客户端的请求，通过改造消息头的字段（14.42节），以改变在此连接上使用的应用协议。紧接在作为101响应结束的空行之后，服务器将立刻切换到改造后的响应头部字段所定义的协议。

> The protocol SHOULD be switched only when it is advantageous to do so. For example, switching to a newer version of HTTP is advantageous over older versions, and switching to a real-time, synchronous protocol might be advantageous when delivering resources that use such features.

协议只 **应该** 切换到更有利的情况。例如，切换到较新版本的HTTP比旧版本更有优势，又如当交付具有实时、同步特性的资源时，切换到具有这些特性的协议可能是有利的。

### 10.2 Successful 2xx （成功）

> This class of status code indicates that the client's request was successfully received, understood, and accepted.

这类状态码表明客户端的请求已被成功接收，理解并接受。

#### 10.2.1 200 OK （正常）

> The request has succeeded. The information returned with the response is dependent on the method used in the request, for example:

请求成功。随响应一起返回的信息取决于请求中使用的方法，例如：

> GET an entity corresponding to the requested resource is sent in the response;
>
> HEAD the entity-header fields corresponding to the requested resource are sent in the response without any message-body;
>
> POST an entity describing or containing the result of the action;
>
> TRACE an entity containing the request message as received by the end server.

**GET** 在响应中发送与所请求的资源对应的实体（entity）；

**HEAD** 在响应中发送与所请求的资源对应的实体头部（entity-header）字段，而不包含任何信息体（message-body）；

**POST** 一个描述或包含了处理结果的实体；

**TRACE** 一个包含终端服务器接收到的请求信息的实体。

#### 10.2.2 201 Created （已创建）

> The request has been fulfilled and resulted in a new resource being created. The newly created resource can be referenced by the URI(s) returned in the entity of the response, with the most specific URI for the resource given by a Location header field. The response SHOULD include an entity containing a list of resource characteristics and location(s) from which the user or user agent can choose the one most appropriate. The entity format is specified by the media type given in the Content-Type header field. The origin server MUST create the resource before returning the 201 status code. If the action cannot be carried out immediately, the server SHOULD respond with 202 (Accepted) response instead.

请求完成，并因此创建了一个新的资源。该资源可由响应实体中返回的一个或多个URL引用，其中与该资源最匹配的URL会被作为头部的 `Location` 字段给出。响应 **应该** 包括一个含有一个列表的实体，该列表描述了所包含资源的特性和其一个或多个地址，用户或用户代理可以从中选择一个最合适的地址。实体格式由头部的 `Content-Type` 字段给出的媒体类型所指定。源服务器 **必须** 在返回201状态码之前创建好所需的资源。如果资源不能被立即创建，那么服务器应该用 `202 (Accepted)` 响应来代替201响应。

> A 201 response MAY contain an ETag response header field indicating the current value of the entity tag for the requested variant just created, see section [14.19](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.19).

一个201响应 **可以** 包含一个 `ETag` 响应头部字段，用于指出刚创建的被请求变量（requested variant）的实体标签（entity tag）的当前值，参见[14.19](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.19)节

#### 10.2.3 202 Accepted （已接受）

> The request has been accepted for processing, but the processing has not been completed. The request might or might not eventually be acted upon, as it might be disallowed when processing actually takes place. There is no facility for re-sending a status code from an asynchronous operation such as this.

该请求已被接受进行处理，但处理尚未完成。该请求最终可能会也可能不会被满足，因为请求可能在实际处理过程中被禁止。这样一种异步机制并没有重发状态码的功能。

> The 202 response is intentionally non-committal. Its purpose is to allow a server to accept a request for some other process (perhaps a batch-oriented process that is only run once per day) without requiring that the user agent's connection to the server persist until the process is completed. The entity returned with this response SHOULD include an indication of the request's current status and either a pointer to a status monitor or some estimate of when the user can expect the request to be fulfilled.

202响应是故意不作承诺（non-committal）的。它的目的在于允许服务器接受对其他进程的请求（也许是一个每天只运行一次的面向批处理（batch-oriented）的进程），而不需要维持与客户代理的连接直到进程完成。这个响应返回的实体 **应该** 包含一个对于请求的当前状态的指示，或者一个指向状态监视器的指针，或一些对于用户请求何时会被满足的估计。

#### 10.2.4 203 Non-Authoritative Information （非权威信息）

> The returned metainformation in the entity-header is not the definitive set as available from the origin server, but is gathered from a local or a third-party copy. The set presented MAY be a subset or superset of the original version. For example, including local annotation information about the resource might result in a superset of the metainformation known by the origin server. Use of this response code is not required and is only appropriate when the response would otherwise be 200 (OK).

在实体头部中返回的元信息（metainformation）并不是从源服务器获得的权威信息的集合，而是从本地或第三方副本收集的。所得的信息集合 **可以** 是原始版本的子集或超集。例如，如果包含对资源的本地标注信息，可能会导致得到一个源服务器已知元信息的超集。使用此响应代码不是必需的，并且该状态码只适于在不能使用 `200 (OK)` 响应的情况下使用。

#### 10.2.5 204 No Content （无内容）

> The server has fulfilled the request but does not need to return an entity-body, and might want to return updated metainformation. The response MAY include new or updated metainformation in the form of entity-headers, which if present SHOULD be associated with the requested variant.

服务器对请求的处理已完成，但没有返回实体主体（entity-body）的需要，并且可能想要返回更新后的元信息。响应 **可以** 在生成实体头部时包含新的或更新后的元信息，如果的确如此，那这些信息 **应该** 与请求变量相关联。

> If the client is a user agent, it SHOULD NOT change its document view from that which caused the request to be sent. This response is primarily intended to allow input for actions to take place without causing a change to the user agent's active document view, although any new or updated metainformation SHOULD be applied to the document currently in the user agent's active view.

如果客户端是一个用户代理，则它 **不应该** 为此（接收到一个204响应）改变文档视图（document view）。尽管任何新的或更新后的元信息 **应该** 被用户代理应用到当前活动的文档视图中，但是这个响应主要是为了允许在不改变用户代理的活动文档视图的情况下为其活动进行输入操作。

> The 204 response MUST NOT include a message-body, and thus is always terminated by the first empty line after the header fields.

204响应 **绝不能** 包含信息体，因此它总会被头部字段之后的第一个空行所终止。

#### 10.2.6 205 Reset Content （内容重置）

> The server has fulfilled the request and the user agent SHOULD reset the document view which caused the request to be sent. This response is primarily intended to allow input for actions to take place via user input, followed by a clearing of the form in which the input is given so that the user can easily initiate another input action. The response MUST NOT include an entity.

服务器对请求的处理已完成，用户代理 **应该** 重置导致该请求被发送的文档的文档视图。该响应主要是为了允许通过用户输入对用户代理的活动进行输入操作，然后清除该输入，以便用户可以很容易地开始另一个输入动作。响应 **绝不能** 包含任何实体。

#### 10.2.7 206 Partial Content （部分内容）

> The server has fulfilled the partial GET request for the resource. The request MUST have included a Range header field (section 14.35) indicating the desired range, and MAY have included an If-Range header field (section [14.27](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.27)) to make the request conditional.

服务器已经处理完了对资源的部分GET请求。该请求 **必须** 包含一个 `Range` 头部字段（14.35节），表示期望的范围，并且 **可以** 包含一个 `If-Range` 头部字段（[14.27](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.27)节）来使请求条件明确。

> The response MUST include the following header fields:
>
> - Either a Content-Range header field (section 14.16) indicating  
> the range included with this response, or a multipart/byteranges  
> Content-Type including Content-Range fields for each part. If a  
> Content-Length header field is present in the response, its  
> value MUST match the actual number of OCTETs transmitted in the  
> message-body.
> - Date
> - ETag and/or Content-Location, if the header would have been sent  
> in a 200 response to the same request
> - Expires, Cache-Control, and/or Vary, if the field-value might  
> differ from that sent in any previous response for the same  
> variant

响应 **必须** 包含以下头部字段：

- 一个 `Content-Range` 头部字段（14.16节），指示该响应包含  
的范围；或者将 `Content-Type` 头部字段置为 `multipart/byteranges` ，  
并在每个部分包含 `Content-Range` 字段。如果在响应头部含有一个  
`Content-Length` 字段，则它的值 **必须** 与在信息体中实际传输  
的 **8比特字节（octet）** 数相匹配。
- `Data`
- `ETag` 和/或 `Content-Location` ，如果头部已经在一个对该  
请求的200响应中被发送。
- `Expires` ， `Cache-Control` ，和/或 `Vary` ，如果字段值（field-value）  
可能与之前对该请求发送的任何响应中的字段值都不同。

> If the 206 response is the result of an If-Range request that used a strong cache validator (see section 13.3.3), the response SHOULD NOT include other entity-headers. If the response is the result of an If-Range request that used a weak validator, the response MUST NOT include other entity-headers; this prevents inconsistencies between cached entity-bodies and updated headers. Otherwise, the response MUST include all of the entity-headers that would have been returned with a 200 (OK) response to the same request.

如果该206响应是对一个使用强缓存验证器（strong cache validator）的 `If-Range` 请求（请参阅第13.3.3节）的回应，则该响应 **不应该** 包含其他实体头部。如果响应是对一个使用弱验证器（weak validator）的 `If-Range` 请求的回应，则该响应 **绝不能** 包含其他实体头部；这可以防止缓存的实体与更新的头部之间不一致。否则，该响应 **必须** 包含对该请求已返回的 `200 (OK)` 响应的全部实体头部。

> A cache MUST NOT combine a 206 response with other previously cached content if the ETag or Last-Modified headers do not match exactly, see [13.5.4](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.5.4).

如果缓存器的 `ETag` 或 `Last-Modified` 头部字段与一个206响应不完全匹配，则 **绝不能** 将该206响应与其他先前的缓存内容合并，见[13.5.4](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.5.4)。

> A cache that does not support the Range and Content-Range headers MUST NOT cache 206 (Partial) responses.

不支持 `Range` 和 `Content-Range` 头部的缓存器 **绝不能** 缓存 `206 (Partial)` 响应。

### 10.3 Redirection 3xx （重定向）

> This class of status code indicates that further action needs to be taken by the user agent in order to fulfill the request. The action required MAY be carried out by the user agent without interaction with the user if and only if the method used in the second request is GET or HEAD. A client SHOULD detect infinite redirection loops, since such loops generate network traffic for each redirection.

这类状态码表明用户代理需要采取进一步行动来完成请求。当且仅当第二个请求中使用的方法是GET或HEAD时，所需的进一步行动 **可以** 由用户代理自动执行，而不与用户进行交互。客户端 **应该** 检测到无限重定向循环，因为这种循环的每个重定向都在浪费网络流量。

> > Note: previous versions of this specification recommended a  
> > maximum of five redirections. Content developers should be aware  
> > that there might be clients that implement such a fixed  
> > limitation.

> 注意：此规范过去的版本建议最多不超过五个重定向。内容开发者应该  
> 意识到，也许有的客户端已经实现了这样一个固定的限制。

#### 10.3.1 300 Multiple Choices （多重选择）

> The requested resource corresponds to any one of a set of representations, each with its own specific location, and agent-driven negotiation information (section 12) is being provided so that the user (or user agent) can select a preferred representation and redirect its request to that location.

所请求的资源对应于一组记录的任意一条，每条记录都有其唯一的地址，并且提供代理驱动（agent-driven）的协商信息（第12节），这使得用户（或用户代理）可以选择一条最优的记录，并重定向到所选的地址。

> Unless it was a HEAD request, the response SHOULD include an entity containing a list of resource characteristics and location(s) from which the user or user agent can choose the one most appropriate. The entity format is specified by the media type given in the Content-Type header field. Depending upon the format and the capabilities of the user agent, selection of the most appropriate choice MAY be performed automatically. However, this specification does not define any standard for such automatic selection.

除非是HEAD请求，否则响应 **应该** 附带一个内含列表的实体，该列表列出了资源的特性和资源所在的地址，用户或用户代理可以从中选择最合适的一个。实体格式由 `Content-Type` 头部字段中给出的媒体类型所指定。用户代理 **可以** 根据其设计和功能，自动选择最合适的选项。但是，该规范没有为这种自动选择定义任何标准。

> If the server has a preferred choice of representation, it SHOULD include the specific URI for that representation in the Location field; user agents MAY use the Location field value for automatic redirection. This response is cacheable unless indicated otherwise.

如果服务器有推荐的记录，它 **应该** 在 `Location` 字段中包含该记录的URI；用户代理 **可以** 使用 `Location` 字段值进行自动重定向。除非另有说明，否则该响应是可缓存的。

#### 10.3.2 301 Moved Permanently （永久转移）

> The requested resource has been assigned a new permanent URI and any future references to this resource SHOULD use one of the returned URIs. Clients with link editing capabilities ought to automatically re-link references to the Request-URI to one or more of the new references returned by the server, where possible. This response is cacheable unless indicated otherwise.

所请求的资源已经被转移到了一个新的永久性的URI，任何将来对这个资源的引用都 **应该** 使用返回的URI中的一个。能够编辑链接的客户端应尽可能将对 `Request-URI` 的引用重新链接到服务器返回的一个或多个新的引用。除非另有说明，否则该响应是可缓存的。

> The new permanent URI SHOULD be given by the Location field in the response. Unless the request method was HEAD, the entity of the response SHOULD contain a short hypertext note with a hyperlink to the new URI(s).

新的永久URI **应该** 在响应的 `Location` 字段给出。除非请求方法是HEAD，否则响应的实体 **应该** 包含一条简短的超文本记录，该记录包含一个转到新URI的超链接。

> If the 301 status code is received in response to a request other than GET or HEAD, the user agent MUST NOT automatically redirect the request unless it can be confirmed by the user, since this might change the conditions under which the request was issued.

如果用户代理接收到一个301状态的响应，且该响应是对一个既非GET亦非HEAD请求的回应，那么除非经过用户的确认，否则用户代理 **绝不能** 自动重定向，因为这可能不符合最初发送请求的条件。

> > Note: When automatically redirecting a POST request after  
> > receiving a 301 status code, some existing HTTP/1.0 user agents  
> > will erroneously change it into a GET request.

> 注意：在收到一个301状态码后，自动重定向一个POST请求时，一些现有  
> 的HTTP/1.0用户代理会错误地将其更改为GET请求。

#### 10.3.3 302 Found （已创建）

> The requested resource resides temporarily under a different URI. Since the redirection might be altered on occasion, the client SHOULD continue to use the Request-URI for future requests. This response is only cacheable if indicated by a Cache-Control or Expires header field.

所请求的资源暂时驻留在另一个URI下。由于重定向可能会被改变，所以客户端 **应该** 继续使用 `Request-URI` 来处理将来的请求。只有在 `Cache-Control` 或 `Expires` 头部字段指明时，该响应才可缓存。

> The temporary URI SHOULD be given by the Location field in the response. Unless the request method was HEAD, the entity of the response SHOULD contain a short hypertext note with a hyperlink to the new URI(s).

临时URI **应该** 在响应的 `Location` 字段给出。除非请求方法是HEAD，否则响应的实体 **应该** 包含一条简短的超文本记录，该记录包含一个转到新URI的超链接。

> If the 302 status code is received in response to a request other than GET or HEAD, the user agent MUST NOT automatically redirect the request unless it can be confirmed by the user, since this might change the conditions under which the request was issued.

如果用户代理接收到一个302状态的响应，且该响应是对一个既非GET亦非HEAD方法的请求的回应，那么除非经过用户的确认，否则用户代理 **绝不能** 自动重定向，因为这可能不符合最初发送请求的条件。

> > Note: RFC 1945 and RFC 2068 specify that the client is not allowed  
> > to change the method on the redirected request.  However, most  
> > existing user agent implementations treat 302 as if it were a 303  
> > response, performing a GET on the Location field-value regardless  
> > of the original request method. The status codes 303 and 307 have  
> > been added for servers that wish to make unambiguously clear which  
> > kind of reaction is expected of the client.

> 注意：尽管RFC 1945和RFC 2068已明确不允许客户端更改重定向请求所使用的请求方  
> 法。但是，现有的多数用户代理实现都将302响应当作303响应处理，无论原始请求方法  
> 是什么，都对 `Location` 字段值发送GET请求。为了满足那些希望明确获知客户端期望何
> 种反应的服务器，状态码303和307已被添加到新的规范中。

#### 10.3.4 303 See Other （查看其它）

> The response to the request can be found under a different URI and SHOULD be retrieved using a GET method on that resource. This method exists primarily to allow the output of a POST-activated script to redirect the user agent to a selected resource. The new URI is not a substitute reference for the originally requested resource. The 303 response MUST NOT be cached, but the response to the second (redirected) request might be cacheable.

对请求的响应可以在另一个URI下被找到，并且 **应该** 使用GET方法通过新的URI重新获取资源。此方法主要用于允许POST方法激活的脚本（POST-activated script）的输出，从而将用户代理重定向到选定的的资源。新的URI并不是最初请求的资源的替代链接。303响应 **绝不能** 被缓存，但对第二个（重定向的）请求的响应可能是可缓存的。

> The different URI SHOULD be given by the Location field in the response. Unless the request method was HEAD, the entity of the response SHOULD contain a short hypertext note with a hyperlink to the new URI(s).

新的URI **应该** 由响应中的 `Location` 字段给出。除非请求方法是HEAD，否则响应的实体 **应该** 包含一条简短的超文本记录，该记录包含一个转到新URI的超链接。

> > Note: Many pre-HTTP/1.1 user agents do not understand the 303  
> > status. When interoperability with such clients is a concern, the  
> > 302 status code may be used instead, since most user agents react  
> > to a 302 response as described here for 303.

> 注意：许多pre-HTTP/1.1用户代理不能理解303状态。如果担忧与这种客户端的  
> 交互性，可以使用302状态码来代替303状态码，因为多数用户代理对302的反应  
> 像对303描述的那样。

#### 10.3.5 304 Not Modified （未修改）

> If the client has performed a conditional GET request and access is allowed, but the document has not been modified, the server SHOULD respond with this status code. The 304 response MUST NOT contain a message-body, and thus is always terminated by the first empty line after the header fields.

如果客户端发送了有条件的GET请求并被允许访问，但文档尚未被修改，则服务器 **应该** 使用此状态码进行响应。304响应 **绝不能** 包含消息体，因此总是在头部字段后的第一个空行后终止。

> The response MUST include the following header fields:
>
> - Date, unless its omission is required by section 14.18.1
>
> If a clockless origin server obeys these rules, and proxies and clients add their own Date to any response received without one (as already specified by [RFC 2068], section [14.19](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.19)), caches will operate correctly.
>
> - ETag and/or Content-Location, if the header would have been sent  
> in a 200 response to the same request
> - Expires, Cache-Control, and/or Vary, if the field-value might  
> differ from that sent in any previous response for the same  
> variant

响应 **必须** 包含以下头部字段：

- `Date` ，除非按第14.18.1节要求省略

如果无时钟的源服务器服从这些规则，并且代理和客户端将它们自己的日期添加到收到的任何的没有日期的响应中（如[RFC 2068]，[14.19]中所述），则缓存将正常运行。

- `ETag` 和/或 `Content-Location` ，如果头部已经在一个对该请求的200响应中被发送。
- `Expires` ， `Cache-Control` ，和/或 `Vary` ，如果字段值可能不同于在以往对该请求的任何响应中被发送的该字段值的变种

If the conditional GET used a strong cache validator (see section 13.3.3), the response SHOULD NOT include other entity-headers. Otherwise (i.e., the conditional GET used a weak validator), the response MUST NOT include other entity-headers; this prevents inconsistencies between cached entity-bodies and updated headers.

If a 304 response indicates an entity not currently cached, then the cache MUST disregard the response and repeat the request without the conditional.

If a cache uses a received 304 response to update a cache entry, the cache MUST update the entry to reflect any new field values given in the response.

#### 10.3.6 305 Use Proxy

The requested resource MUST be accessed through the proxy given by the Location field. The Location field gives the URI of the proxy. The recipient is expected to repeat this single request via the proxy. 305 responses MUST only be generated by origin servers.

> Note: RFC 2068 was not clear that 305 was intended to redirect a  
> single request, and to be generated by origin servers only.  Not  
> observing these limitations has significant security consequences.

#### 10.3.7 306 (Unused) （已停止使用）

> The 306 status code was used in a previous version of the specification, is no longer used, and the code is reserved.

306状态码曾被用于先前版本的规范，现已不再使用，但仍保留该代码。

#### 10.3.8 307 Temporary Redirect

The requested resource resides temporarily under a different URI. Since the redirection MAY be altered on occasion, the client SHOULD continue to use the Request-URI for future requests. This response is only cacheable if indicated by a Cache-Control or Expires header field.

The temporary URI SHOULD be given by the Location field in the response. Unless the request method was HEAD, the entity of the response SHOULD contain a short hypertext note with a hyperlink to the new URI(s) , since many pre-HTTP/1.1 user agents do not understand the 307 status. Therefore, the note SHOULD contain the information necessary for a user to repeat the original request on the new URI.

If the 307 status code is received in response to a request other than GET or HEAD, the user agent MUST NOT automatically redirect the request unless it can be confirmed by the user, since this might change the conditions under which the request was issued.

### 10.4 Client Error 4xx （客户端错误）

The 4xx class of status code is intended for cases in which the client seems to have erred. Except when responding to a HEAD request, the server SHOULD include an entity containing an explanation of the error situation, and whether it is a temporary or permanent condition. These status codes are applicable to any request method. User agents SHOULD display any included entity to the user.

If the client is sending data, a server implementation using TCP SHOULD be careful to ensure that the client acknowledges receipt of the packet(s) containing the response, before the server closes the input connection. If the client continues sending data to the server after the close, the server's TCP stack will send a reset packet to the client, which may erase the client's unacknowledged input buffers before they can be read and interpreted by the HTTP application.

#### 10.4.1 400 Bad Request

The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.

#### 10.4.2 401 Unauthorized （未经许可）

The request requires user authentication. The response MUST include a WWW-Authenticate header field (section 14.47) containing a challenge applicable to the requested resource. The client MAY repeat the request with a suitable Authorization header field (section [14.8](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.8)). If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. If the 401 response contains the same challenge as the prior response, and the user agent has already attempted authentication at least once, then the user SHOULD be presented the entity that was given in the response, since that entity might include relevant diagnostic information. HTTP access authentication is explained in "HTTP Authentication: Basic and Digest Access Authentication" [[43]](https://www.w3.org/Protocols/rfc2616/rfc2616-sec17.html#bib43).

#### 10.4.3 402 Payment Required （需要支付）

This code is reserved for future use.

#### 10.4.4 403 Forbidden （禁止访问）

The server understood the request, but is refusing to fulfill it. Authorization will not help and the request SHOULD NOT be repeated. If the request method was not HEAD and the server wishes to make public why the request has not been fulfilled, it SHOULD describe the reason for the refusal in the entity. If the server does not wish to make this information available to the client, the status code 404 (Not Found) can be used instead.

#### 10.4.5 404 Not Found （未找到）

The server has not found anything matching the Request-URI. No indication is given of whether the condition is temporary or permanent. The 410 (Gone) status code SHOULD be used if the server knows, through some internally configurable mechanism, that an old resource is permanently unavailable and has no forwarding address. This status code is commonly used when the server does not wish to reveal exactly why the request has been refused, or when no other response is applicable.

#### 10.4.6 405 Method Not Allowed （不允许的请求方法）

The method specified in the Request-Line is not allowed for the resource identified by the Request-URI. The response MUST include an Allow header containing a list of valid methods for the requested resource.

#### 10.4.7 406 Not Acceptable （不接受）

The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request.

Unless it was a HEAD request, the response SHOULD include an entity containing a list of available entity characteristics and location(s) from which the user or user agent can choose the one most appropriate. The entity format is specified by the media type given in the Content-Type header field. Depending upon the format and the capabilities of the user agent, selection of the most appropriate choice MAY be performed automatically. However, this specification does not define any standard for such automatic selection.

> Note: HTTP/1.1 servers are allowed to return responses which are  
> not acceptable according to the accept headers sent in the  
> request. In some cases, this may even be preferable to sending a  
> 406 response. User agents are encouraged to inspect the headers of  
> an incoming response to determine if it is acceptable.

If the response could be unacceptable, a user agent SHOULD temporarily stop receipt of more data and query the user for a decision on further actions.

#### 10.4.8 407 Proxy Authentication Required （要求验证代理身份）

This code is similar to 401 (Unauthorized), but indicates that the client must first authenticate itself with the proxy. The proxy MUST return a Proxy-Authenticate header field (section [14.33](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.33)) containing a challenge applicable to the proxy for the requested resource. The client MAY repeat the request with a suitable Proxy-Authorization header field (section [14.34](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.34)). HTTP access authentication is explained in "HTTP Authentication: Basic and Digest Access Authentication" [[43]](https://www.w3.org/Protocols/rfc2616/rfc2616-sec17.html#bib43).

#### 10.4.9 408 Request Timeout （请求超时）

The client did not produce a request within the time that the server was prepared to wait. The client MAY repeat the request without modifications at any later time.

#### 10.4.10 409 Conflict （访问冲突）

The request could not be completed due to a conflict with the current state of the resource. This code is only allowed in situations where it is expected that the user might be able to resolve the conflict and resubmit the request. The response body SHOULD include enough

information for the user to recognize the source of the conflict. Ideally, the response entity would include enough information for the user or user agent to fix the problem; however, that might not be possible and is not required.

Conflicts are most likely to occur in response to a PUT request. For example, if versioning were being used and the entity being PUT included changes to a resource which conflict with those made by an earlier (third-party) request, the server might use the 409 response to indicate that it can't complete the request. In this case, the response entity would likely contain a list of the differences between the two versions in a format defined by the response Content-Type.

#### 10.4.11 410 Gone

The requested resource is no longer available at the server and no forwarding address is known. This condition is expected to be considered permanent. Clients with link editing capabilities SHOULD delete references to the Request-URI after user approval. If the server does not know, or has no facility to determine, whether or not the condition is permanent, the status code 404 (Not Found) SHOULD be used instead. This response is cacheable unless indicated otherwise.

The 410 response is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable and that the server owners desire that remote links to that resource be removed. Such an event is common for limited-time, promotional services and for resources belonging to individuals no longer working at the server's site. It is not necessary to mark all permanently unavailable resources as "gone" or to keep the mark for any length of time -- that is left to the discretion of the server owner.

#### 10.4.12 411 Length Required （要求指示长度）

The server refuses to accept the request without a defined Content- Length. The client MAY repeat the request if it adds a valid Content-Length header field containing the length of the message-body in the request message.

#### 10.4.13 412 Precondition Failed （先决条件未满足）

The precondition given in one or more of the request-header fields evaluated to false when it was tested on the server. This response code allows the client to place preconditions on the current resource metainformation (header field data) and thus prevent the requested method from being applied to a resource other than the one intended.

#### 10.4.14 413 Request Entity Too Large （请求实体过大）

The server is refusing to process a request because the request entity is larger than the server is willing or able to process. The server MAY close the connection to prevent the client from continuing the request.

If the condition is temporary, the server SHOULD include a Retry- After header field to indicate that it is temporary and after what time the client MAY try again.

#### 10.4.15 414 Request-URI Too Long

The server is refusing to service the request because the Request-URI is longer than the server is willing to interpret. This rare condition is only likely to occur when a client has improperly converted a POST request to a GET request with long query information, when the client has descended into a URI "black hole" of redirection (e.g., a redirected URI prefix that points to a suffix of itself), or when the server is under attack by a client attempting to exploit security holes present in some servers using fixed-length buffers for reading or manipulating the Request-URI.

#### 10.4.16 415 Unsupported Media Type

The server is refusing to service the request because the entity of the request is in a format not supported by the requested resource for the requested method.

#### 10.4.17 416 Requested Range Not Satisfiable

A server SHOULD return a response with this status code if a request included a Range request-header field (section 14.35), and none of the range-specifier values in this field overlap the current extent of the selected resource, and the request did not include an If-Range request-header field. (For byte-ranges, this means that the first- byte-pos of all of the byte-range-spec values were greater than the current length of the selected resource.)

When this status code is returned for a byte-range request, the response SHOULD include a Content-Range entity-header field specifying the current length of the selected resource (see section [14.16](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16)). This response MUST NOT use the multipart/byteranges content- type.

#### 10.4.18 417 Expectation Failed

The expectation given in an Expect request-header field (see section 14.20) could not be met by this server, or, if the server is a proxy, the server has unambiguous evidence that the request could not be met by the next-hop server.

### 10.5 Server Error 5xx

Response status codes beginning with the digit "5" indicate cases in which the server is aware that it has erred or is incapable of performing the request. Except when responding to a HEAD request, the server SHOULD include an entity containing an explanation of the error situation, and whether it is a temporary or permanent condition. User agents SHOULD display any included entity to the user. These response codes are applicable to any request method.

#### 10.5.1 500 Internal Server Error

The server encountered an unexpected condition which prevented it from fulfilling the request.

#### 10.5.2 501 Not Implemented

The server does not support the functionality required to fulfill the request. This is the appropriate response when the server does not recognize the request method and is not capable of supporting it for any resource.

#### 10.5.3 502 Bad Gateway

The server, while acting as a gateway or proxy, received an invalid response from the upstream server it accessed in attempting to fulfill the request.

#### 10.5.4 503 Service Unavailable

The server is currently unable to handle the request due to a temporary overloading or maintenance of the server. The implication is that this is a temporary condition which will be alleviated after some delay. If known, the length of the delay MAY be indicated in a Retry-After header. If no Retry-After is given, the client SHOULD handle the response as it would for a 500 response.

> Note: The existence of the 503 status code does not imply that a  
> server must use it when becoming overloaded. Some servers may wish  
> to simply refuse the connection.

#### 10.5.5 504 Gateway Timeout

The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server specified by the URI (e.g. HTTP, FTP, LDAP) or some other auxiliary server (e.g. DNS) it needed to access in attempting to complete the request.

> Note: Note to implementors: some deployed proxies are known to  
> return 400 or 500 when DNS lookups time out.

#### 10.5.6 505 HTTP Version Not Supported

The server does not support, or refuses to support, the HTTP protocol version that was used in the request message. The server is indicating that it is unable or unwilling to complete the request using the same major version as the client, as described in section [3.1](https://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.1), other than with this error message. The response SHOULD contain an entity describing why that version is not supported and what other protocols are supported by that server.
